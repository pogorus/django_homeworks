from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    image = models.ImageField()
    release_date = models.DateField()
    lte_exist = models.BooleanField()
    slug = models.SlugField()

