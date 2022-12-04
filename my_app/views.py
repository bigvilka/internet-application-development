from django.shortcuts import render
from .models import Book

# Create your views here.


def index(request):
    books = []
    filter = "Название книги"
    if request.method == "POST":
        name = request.POST.get("name")
        if name:
            books = Book.objects.filter(name = name)
            filter = name
        else:
            books = Book.objects.all().values()
    else:
        books = Book.objects.all().values()

    data = {"books": books, "filter": filter}
    return render(request, "index.html", context=data)