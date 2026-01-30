from django.urls import path  # ✅ path MUST be imported
from .views import BookList

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # ✅ exact path usage
]
