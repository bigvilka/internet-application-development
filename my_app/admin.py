from django.contrib import admin
from .models import LibraryHall, Rack, Book

# Register your models here.

admin.site.register(LibraryHall)
admin.site.register(Rack)
admin.site.register(Book)