# Delete Operation

**Python command:**
```python
from bookshelf.models import Book
retrieved_book.delete()
print(Book.objects.filter(id=retrieved_book.id).exists())
```

**Output:**
```
False
```
