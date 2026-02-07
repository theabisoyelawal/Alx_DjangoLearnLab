from rest_framework import serializers
from .models import Author, Book
from datetime import datetime


class BookSerializer(serializers.ModelSerializer):
    """
    Serializes all fields of the Book model.
    Includes custom validation to prevent future publication years.
    """

    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        """
        Ensures the publication year is not in the future.
        """
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future."
            )
        return value

class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializes Author model.
    Includes a nested BookSerializer to show related books.
    """

    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
