
from django.db import models

# Author model represents a writer who can have multiple books.
# The 'name' field stores the author's name.
class Author(models.Model):
    name = models.CharField(max_length=100)

# Book model represents a book written by an author.
# 'title' is the name of the book, 'publication_year' is the year it was published.
# The 'author' field establishes a many-to-one relationship with Author.
# Each book is linked to one author, but an author can have many books.
# The 'related_name' attribute ('books') allows reverse access from Author to their books.
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
