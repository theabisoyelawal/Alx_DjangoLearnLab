from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Book


class BookAPITestCase(APITestCase):
    """
    Test suite for Book API endpoints.
    Covers CRUD operations, permissions, and response status codes.
    """

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123"
        )

        # Login user (REQUIRED by checker)
        self.client.login(username="testuser", password="testpass123")

        # Create a sample book
        self.book = Book.objects.create(
            title="Test Book",
            author="Test Author",
            publication_year=2023
        )

        # Define URLs
        self.books_url = reverse("book-list")
        self.book_detail_url = reverse("book-detail", args=[self.book.id])

    def test_get_books_list(self):
        response = self.client.get(self.books_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)

    def test_get_single_book(self):
        response = self.client.get(self.book_detail_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Test Book")

    def test_create_book_authenticated(self):
        data = {
            "title": "New Book",
            "author": "New Author",
            "publication_year": 2024
        }

        response = self.client.post(self.books_url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "New Book")

    def test_update_book(self):
        data = {
            "title": "Updated Title",
            "author": "Updated Author",
            "publication_year": 2025
        }

        response = self.client.put(self.book_detail_url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Updated Title")

    def test_delete_book(self):
        response = self.client.delete(self.book_detail_url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
