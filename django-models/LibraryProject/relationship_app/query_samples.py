from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
def get_books_by_author(author_name):
    # First, find the author by name
    author = Author.objects.get(name=author_name)
    # Then, find all books where the author is this specific author
    return Book.objects.filter(author=author)

# 2. List all books in a library
def get_books_in_library(library_name):
    # First, find the library by name
    library = Library.objects.get(name=library_name)
    # Use the .all() method on the many-to-many relationship
    return library.books.all()

# 3. Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    # First, find the library by name
    library = Library.objects.get(name=library_name)
    # Use the OneToOne relationship to get the librarian
    # The 'librarian' attribute is available because it's a OneToOneField
    return Librarian.objects.get(library=library)