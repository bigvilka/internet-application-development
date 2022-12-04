from django.db import models

# Create your models here.

class LibraryHall(models.Model):
    short_name = models.CharField(max_length=32)
    full_name = models.TextField()


class Rack(models.Model):
    library_hall = models.ForeignKey(LibraryHall, on_delete = models.CASCADE)


class Book(models.Model):
    name = models.CharField(max_length=256)
    authors = models.CharField(max_length=256)
    volume = models.IntegerField(null=True, blank=True)
    path = models.IntegerField(null=True, blank=True)
    isbn = models.CharField(max_length=256)
    year = models.DateField()
    rack = models.ForeignKey(Rack, on_delete = models.CASCADE)
    shelf = models.IntegerField()
    number = models.IntegerField()