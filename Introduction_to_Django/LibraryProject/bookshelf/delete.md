# Delete Operation

**Python command:**
```python
retrieved_book.delete()
print(Book.objects.filter(id=retrieved_book.id).exists())
```

**Output:**
```
False
```
