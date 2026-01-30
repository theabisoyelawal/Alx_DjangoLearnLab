from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

# Create a router and register the viewset
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Existing BookList view
    path('books/', BookList.as_view(), name='book-list'),

    # Include all router URLs (for full CRUD)
    path('', include(router.urls)),
]
