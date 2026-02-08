from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework
from .models import Book
from .serializers import BookSerializer



class BookListView(generics.ListAPIView):
    """
    List all books with filtering, searching, and ordering support.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Enable filtering, searching, and ordering
    filter_backends = [
        rest_framework.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]

    # Fields allowed for filtering
    filterset_fields = ['title', 'author', 'publication_year']

    # Fields allowed for search
    search_fields = ['title', 'author__name']

    # Fields allowed for ordering
    ordering_fields = ['title', 'publication_year']



class BookDetailView(generics.RetrieveAPIView):
    """
    Retrieve a single book.
    Read-only access for unauthenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookCreateView(generics.CreateAPIView):
    """
    Create a new book.
    Authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookUpdateView(generics.UpdateAPIView):
    """
    Update an existing book.
    Authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookDeleteView(generics.DestroyAPIView):
    """
    Delete a book.
    Authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
