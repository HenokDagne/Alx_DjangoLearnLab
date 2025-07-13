# Create Operation

**Python command:**
```python
from bookshelf.models import Book
book = Book.objects.create(title="Django Basics", author="John Doe", publication_year=2024)
print(book)
```

**Output:**
```
<Book: Django Basics>
```
