import sys
import os

# Set up Django project path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoModels.settings")

import django
django.setup()

from relationship_app.models import Book, Author, Library, Librarian


def get_books_by_author(author_name):
    """
    Query all books by a specific author.
    
    Args:
        author_name (str): The name of the author to filter books by.
    """
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        print(f"Books by {author_name}:")
        for book in books:
            print(f"Title: {book.title}")
    except Author.DoesNotExist:
        print(f"No author found with name: {author_name}")
        print()
        

def list_all_books_in_library(library_name):
    """
    List all books in a specific library.
    
    Args:
        library_name (str): The name of the library to retrieve books from.
    """
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all() 
        print(f"Books in {library_name}:")
        for book in books:
            print(f"Title: {book.title}, By: {book.author.name}")
    except Library.DoesNotExist:
        print(f"No library found with name: {library_name}")
        print()
        

def get_librarian_for_library(library_name):
    """
    Retrieve the librarian for a specific library.
    
    Args:
        library_name (str): The name of the library to retrieve the librarian for.
    """
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library) 
        print(f"Librarian for {library_name}: {librarian.name}")
    except Library.DoesNotExist:
        print(f"No library found with name: {library_name}")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to the library {library_name}")


if __name__ == "__main__":
    
    get_books_by_author("Chinua Achebe")
    list_all_books_in_library("Novel")
    get_librarian_for_library("Spiritual")