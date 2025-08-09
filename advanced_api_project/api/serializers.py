
from rest_framework import serializers
from .models import Author, Book

# BookSerializer converts Book model instances to and from JSON representations.
# It serializes all fields of the Book model, including the author reference.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  # Serializes all fields defined in the Book model

# AuthorSerializer serializes Author model instances.
# It includes the author's name and a nested list of their books.
# The 'books' field uses BookSerializer to represent related Book objects.
# The relationship between Author and Book is handled by the 'books' field,
# which is set to many=True (since an author can have multiple books) and read_only=True
# (books are not created/updated through the AuthorSerializer).
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ['name', 'books']

