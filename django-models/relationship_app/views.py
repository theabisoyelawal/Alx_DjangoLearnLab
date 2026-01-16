from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import redirect
from django.shortcuts import render
from .models import Book  # make sure you have a Book model
from django.views.generic import DetailView
from .models import Library

def list_books(request):
    books = Book.objects.all()  # get all books from database
    return render(request, 'relationship_app/list_books.html', {'books': books})
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # log the user in immediately
            return redirect('list_books')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})
from django.contrib.auth import authenticate

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('list_books')
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})
def logout_view(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')

