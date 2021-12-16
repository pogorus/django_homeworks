from django.core.paginator import Paginator
from django.shortcuts import render
from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    book_objects = Book.objects.all()
    Paginator(book_objects, 1)
    context = {
        'book': book_objects
    }
    return render(request, template, context)

def pub_date_view(request):

