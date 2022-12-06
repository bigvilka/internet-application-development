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


def rack_order(request):
    books = Book.objects.all().order_by("rack_id").values()
    racks = {}
    for book in books:
        if book['rack_id'] in racks:
            racks[book['rack_id']].append(book['name'])
        else:
            racks[book['rack_id']] = [book['name']]

    data = {"racks": racks}
    return render(request, "order.html", context=data)