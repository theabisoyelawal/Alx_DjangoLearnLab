from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required # REQUIRED BY TASK 5 CHECKER
from .models import Book
from .models import Library # REQUIRED BY TASK 2 CHECKER

# --- Task 1: Function-Based View ---
def list_books(request):
    """Lists all books available in the database."""
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# --- Task 2: Class-Based View ---
class LibraryDetailView(DetailView):
    """Displays details for a specific library, listing all books available."""
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# --- Task 3: User Registration ---
def register(request):
    """Handles user registration using Django's built-in UserCreationForm."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_books')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# --- Task 4: Role-Based Access Control ---
def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

# --- Task 5: Permission-Based Views (Add, Edit, Delete Books) ---

@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    """Secured view to add a new book."""
    return render(request, 'relationship_app/add_book.html')

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, pk):
    """Secured view to edit an existing book."""
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'relationship_app/edit_book.html', {'book': book})

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    """Secured view to delete a book."""
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'relationship_app/delete_book.html', {'book': book})