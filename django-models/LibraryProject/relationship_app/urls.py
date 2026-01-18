from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    # FBV
    path('books/', list_books, name='list_books'),
    # CBV
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]