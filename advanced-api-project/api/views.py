from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import Book
from .serializers import BookSerializer


class BookListView(generics.ListAPIView):
    """
    Shows all books.
    Anyone can access this view.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookDetailView(generics.RetrieveAPIView):
    """
    Shows one book using its ID.
    Anyone can access this view.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookCreateView(generics.CreateAPIView):
    """
    Creates a new book.
    Only logged-in users can do this.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookUpdateView(generics.UpdateAPIView):
    """
    Updates an existing book.
    Only logged-in users can do this.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookDeleteView(generics.DestroyAPIView):
    """
    Deletes a book.
    Only logged-in users can do this.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
