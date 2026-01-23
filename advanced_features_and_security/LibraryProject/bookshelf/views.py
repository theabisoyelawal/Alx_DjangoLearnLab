from django.shortcuts import render
from .forms import ExampleForm
from django.contrib.auth.decorators import permission_required
from .models import Book

def example_form_view(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Do something safely with form.cleaned_data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            return render(request, "bookshelf/form_success.html", {"name": name})
    else:
        form = ExampleForm()
    return render(request, "bookshelf/form_example.html", {"form": form})

@permission_required("bookshelf.can_view", raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books})
@permission_required("bookshelf.can_create", raise_exception=True)
def create_book(request):
    return render(request, "bookshelf/create_book.html")
@permission_required("bookshelf.can_edit", raise_exception=True)
def edit_book(request, book_id):
    return render(request, "bookshelf/edit_book.html")
@permission_required("bookshelf.can_delete", raise_exception=True)
def delete_book(request, book_id):
    return render(request, "bookshelf/delete_book.html")
