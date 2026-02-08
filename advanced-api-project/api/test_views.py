from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from api.models import Book

# Django automatically creates and uses a separate test database
# when running tests with `python manage.py test`

class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword"
        )

        # Create sample books
        self.book1 = Book.objects.create(
            title="Django for Beginners",
            author="William",
            publication_year=2020
        )

        self.book2 = Book.objects.create(
            title="Advanced Django",
            author="Jane",
            publication_year=2023
        )

        # URLs
        self.list_url = reverse("book-list")
        self.detail_url = reverse("book-detail", args=[self.book1.id])

    # ✅ Test book list (GET)
    def test_get_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # ✅ Test book creation (POST) – requires authentication
    def test_create_book_authenticated(self):
        self.client.login(username="testuser", password="testpassword")

        data = {
            "title": "New Book",
            "author": "Author Name",
            "publication_year": 2024
        }

        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # ❌ Test book creation without authentication
    def test_create_book_unauthenticated(self):
        data = {
            "title": "Unauthorized Book",
            "author": "Unknown",
            "publication_year": 2024
        }

        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # ✅ Test update book
    def test_update_book(self):
        self.client.login(username="testuser", password="testpassword")

        data = {
            "title": "Updated Django Book",
            "author": "William",
            "publication_year": 2021
        }

        response = self.client.put(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # ✅ Test delete book
    def test_delete_book(self):
        self.client.login(username="testuser", password="testpassword")

        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    # 🔍 Test filtering
    def test_filter_books_by_author(self):
        response = self.client.get(self.list_url + "?author=Jane")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # 🔍 Test search
    def test_search_books(self):
        response = self.client.get(self.list_url + "?search=Django")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # 🔄 Test ordering
    def test_order_books_by_publication_year(self):
        response = self.client.get(self.list_url + "?ordering=publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
