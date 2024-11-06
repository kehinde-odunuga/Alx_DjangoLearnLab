# Delete a Book Instance

## Command
```python

from bookshelf.models import Book

# Delete the book instance
book.delete()

# To retrieve all books to confirm deletion
Book.objects.all()

# Expected Output:
# <QuerySet []> 