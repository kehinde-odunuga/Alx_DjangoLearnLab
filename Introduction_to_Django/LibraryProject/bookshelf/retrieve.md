# Retrieve a Book Instance

## Command
```python

# Retrieve the title of the book
book = Book.objects.get(title="1984")
book.title, retrieved_book.author, retrieved_book.publication_year

# Expected Output:
# ('1984', 'George Orwell', 1949)