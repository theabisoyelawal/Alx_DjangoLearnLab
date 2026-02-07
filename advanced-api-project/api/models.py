from django.db import models


class Author(models.Model):
    """
    Author model represents a writer.
    One author can have multiple books.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book model represents a book written by an author.
    Each book is linked to one author.
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()

    # Foreign key creates a one-to-many relationship:
    # One Author -> Many Books
    author = models.ForeignKey(
        Author,
        related_name='books',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title
