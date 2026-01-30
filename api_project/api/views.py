from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides all CRUD operations for Book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

