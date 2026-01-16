# LibraryProject/relationship_app/query_samples.py

from LibraryProject.relationship_app.models import Author, Book, Library, Librarian

# 1️⃣ Query all books by a specific author
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        return author.books.all()
    except Author.DoesNotExist:
        return f"No author found with the name '{author_name}'"

# 2️⃣ List all books in a library
def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()
    except Library.DoesNotExist:
        return f"No library found with the name '{library_name}'"

# 3️⃣ Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.librarian
    except Library.DoesNotExist:
        return f"No library found with the name '{library_name}'"
    except Librarian.DoesNotExist:
        return f"No librarian assigned to '{library_name}'"
