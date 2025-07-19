import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        return list(Book.objects.filter(author=author))
    except Author.DoesNotExist:
        return []

# List all books in a library
def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return list(library.books.all())
    except Library.DoesNotExist:
        return []

# Retrieve the librarian for a library
def librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return getattr(library, 'librarian', None)
    except Library.DoesNotExist:
        return None

# Example usage (uncomment to test)
# print(books_by_author('Author Name'))
# print(books_in_library('Library Name'))
# print(librarian_for_library('Library Name'))
