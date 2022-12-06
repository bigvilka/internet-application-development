from django.db import models

# Create your models here.

class LibraryHall(models.Model):
    class Meta:
        verbose_name = 'Библиотечный зал'
        verbose_name_plural = 'Библиотечные залы'
        ordering = ['id']

    short_name = models.CharField(max_length=32, verbose_name="Краткое название зала")
    full_name = models.TextField(verbose_name="Полное название зала")


class Rack(models.Model):
    class Meta:
        verbose_name = 'Стеллаж'
        verbose_name_plural = 'Стеллажи'
        ordering = ['id']

    library_hall = models.ForeignKey(LibraryHall, on_delete = models.CASCADE, verbose_name="Номер зала")
    id = models.IntegerField(primary_key=True, verbose_name="Номер стеллажа")


class Book(models.Model):
    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['name']

    name = models.CharField(max_length=256, verbose_name="Название книги")
    authors = models.CharField(max_length=256, verbose_name="Авторы")
    volume = models.IntegerField(null=True, blank=True, verbose_name="Том")
    path = models.IntegerField(null=True, blank=True, verbose_name="Часть")
    isbn = models.CharField(max_length=256, verbose_name="ISBN")
    year = models.DateField(verbose_name="Год издания")
    rack = models.ForeignKey(Rack, on_delete = models.DO_NOTHING, to_field="id", verbose_name="Номер стеллажа")
    shelf = models.IntegerField(verbose_name="Номер полки стеллажа")
    number = models.IntegerField(verbose_name="Количество экземпляров")