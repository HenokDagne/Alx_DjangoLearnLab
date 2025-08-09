from rest_framework import serializers
from .models import Author, Book

# BookSerializer serializes all fields of the Book model.
# Includes custom validation to ensure publication_year is not in the future.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        from datetime import datetime
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

# AuthorSerializer serializes the name field and includes a nested list of books using BookSerializer.
# Demonstrates handling of nested relationships between Author and Book.
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']

# The AuthorSerializer uses the 'books' related_name from the Book model to dynamically serialize all books for an author.
# This setup allows for easy representation of nested objects and complex data structures in API responses.
