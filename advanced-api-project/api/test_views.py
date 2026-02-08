from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Book


class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123"
        )

        # Create a book
        self.book = Book.objects.create(
            title="Test Book",
            author="Test Author",
            publication_year=2023
        )

        # URLs
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
        self.client.force_authenticate(user=self.user)

        data = {
            "title": "New Book",
            "author": "New Author",
            "publication_year": 2024
        }

        response = self.client.post(self.books_url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "New Book")

    def test_create_book_unauthenticated(self):
        data = {
            "title": "Unauthorized Book",
            "author": "No Auth",
            "publication_year": 2024
        }

        response = self.client.post(self.books_url, data)

        self.assertEqual
