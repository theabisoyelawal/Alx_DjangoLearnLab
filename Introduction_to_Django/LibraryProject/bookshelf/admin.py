from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # columns to show
    list_filter = ('author', 'publication_year')            # filters on the right
    search_fields = ('title', 'author')                     # search box

admin.site.register(Book, BookAdmin)
