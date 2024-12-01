from django.db import models

# Author Model: Represents an author of books.
# Fields:
# - name: The name of the author.
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Book Model: Represents a book written by an author.
# Fields:
# - title: The title of the book.
# - publication_year: The year the book was published.
# - author: A foreign key to the Author model, representing the relationship that a book is written by one author.
class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    author = models.ForeignKey(
        Author, 
        on_delete=models.CASCADE, # Deletes books when the associated author is deleted.
        related_name='books' # Enables reverse lookup from Author to their related books.
    )

    def __str__(self):
        return self.title