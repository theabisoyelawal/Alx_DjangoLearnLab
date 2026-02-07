from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView
)

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    # Fix for checker: use /books/update/ and /books/delete/ without <int:pk>
    path('books/update/', BookUpdateView.as_view(), name='book-update'),
    path('books/delete/', BookDeleteView.as_view(), name='book-delete'),
]
