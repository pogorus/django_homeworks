import pytest
from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Student, Course


@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory

@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory


@pytest.mark.django_db
def test_get_one_course(client, course_factory):
    courses = course_factory(_quantity=10)
    course_id = courses[0].id
    response = client.get(f'/api/v1/courses/{course_id}/')
    assert response.status_code == 200
    data = response.json()
    assert data['name'] == courses[0].name


@pytest.mark.django_db
def test_get_courses(client, course_factory):
    courses = course_factory(_quantity=10)
    response = client.get('/api/v1/courses/')
    assert response.status_code == 200
    data = response.json()
    assert len(data) == len(courses)
    for i, course in enumerate(data):
        assert course['name'] == courses[i].name


@pytest.mark.django_db
def test_id_filter(client, course_factory):
    courses = course_factory(_quantity=10)
    course_id = courses[0].id
    response = client.get(f'/api/v1/courses/?id={course_id}')
    assert response.status_code == 200
    data = response.json()
    assert data[0]['name'] == courses[0].name


@pytest.mark.django_db
def test_name_filter(client, course_factory):
    courses = course_factory(_quantity=10)
    course_name = courses[0].name
    response = client.get(f'/api/v1/courses/?name={course_name}')
    assert response.status_code == 200
    data = response.json()
    assert data[0]['id'] == courses[0].id


@pytest.mark.django_db
def test_create_course(client):
    count = Course.objects.count()
    response = client.post('/api/v1/courses/', data={'name': 'Test Course'})
    assert response.status_code == 201
    assert Course.objects.count() == count + 1
    data = client.get('/api/v1/courses/').json()
    assert data[0]['name'] == 'Test Course'


@pytest.mark.django_db
def test_update_course(client, course_factory):
    courses = course_factory(_quantity=10)
    course_id = courses[0].id
    response = client.patch(f'/api/v1/courses/{course_id}/', data={'name': 'Update Course'})
    assert response.status_code == 200
    data = client.get('/api/v1/courses/').json()
    assert data[0]['name'] == 'Update Course'


@pytest.mark.django_db
def test_delete_course(client, course_factory):
    courses = course_factory(_quantity=10)
    course_id = courses[0].id
    response = client.delete(f'/api/v1/courses/{course_id}/')
    assert response.status_code == 204
    data = client.get('/api/v1/courses/').json()
    assert len(data) == len(courses) - 1