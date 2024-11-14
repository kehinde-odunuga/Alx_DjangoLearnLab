
# Create book instatnce
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Display the created instance
book 

# Expected Output:
# (1984 by George Orwell in 1949)

---------------------------------------

# Retrieve the title of the book
book = Book.objects.get(title="1984")
book.title, retrieved_book.author, retrieved_book.publication_year

# Expected Output:
# ('1984', 'George Orwell', 1949)

---------------------------------------

# Update the title of the book
book.title = "Nineteen Eighty-Four"
book.save()

# Display updated title
book.title  

## Expected Output
# 'Nineteen Eighty-Four'

---------------------------------------

# Delete the book instance
book.delete()

# To retrieve all books to confirm deletion
Book.objects.all()

# Expected Output:
# <QuerySet []> 