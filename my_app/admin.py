from django.contrib import admin
from .models import LibraryHall, Rack, Book

# Register your models here.

class LibraryHallAdmin(admin.ModelAdmin):
    list_display = ('short_name',)
    list_display_links = ('short_name',)
    search_fields = ('short_name', 'full_name')


class RackAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)
    search_fields = ('id', 'library_hall')


class BookAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name', 'authors', 'isbn', 'rack')


admin.site.register(LibraryHall, LibraryHallAdmin)
admin.site.register(Rack, RackAdmin)
admin.site.register(Book, BookAdmin)