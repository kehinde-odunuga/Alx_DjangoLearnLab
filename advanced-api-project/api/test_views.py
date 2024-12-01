from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Book, Author
from django.contrib.auth.models import User


class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        
        # Create an author
        self.author = Author.objects.create(name="J.K. Rowling")
        
        # Create some books
        self.book1 = Book.objects.create(title="Harry Potter 1", author=self.author, publication_year=1997)
        self.book2 = Book.objects.create(title="Harry Potter 2", author=self.author, publication_year=1998)
        
        # Define endpoints
        self.list_url = reverse('book-list')  # Adjust name to match your URLconf
        self.detail_url = lambda pk: reverse('book-detail', kwargs={'pk': pk})


# Test List Endpoint
def test_list_books(self):
    response = self.client.get(self.list_url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(response.data), 2)  # Verify both books are returned

# Test Create Endpoint
def test_create_book(self):
    self.client.login(username="testuser", password="testpassword")  # Authenticate user
    data = {"title": "New Book", "author": self.author.id, "publication_year": 2000}
    response = self.client.post(self.list_url, data)
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(Book.objects.count(), 3)  # Ensure a new book is added

# Test Retrieve Endpoint
def test_retrieve_book(self):
    response = self.client.get(self.detail_url(self.book1.id))
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data['title'], "Harry Potter 1")

# Test Update Endpoint
def test_update_book(self):
    self.client.login(username="testuser", password="testpassword")
    data = {"title": "Updated Title", "author": self.author.id, "publication_year": 2001}
    response = self.client.put(self.detail_url(self.book1.id), data)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.book1.refresh_from_db()
    self.assertEqual(self.book1.title, "Updated Title")

# Test Delete Endpoint
def test_delete_book(self):
    self.client.login(username="testuser", password="testpassword")
    response = self.client.delete(self.detail_url(self.book1.id))
    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    self.assertEqual(Book.objects.count(), 1)  # Only one book should remain


# Test Filtering by Title
def test_filter_books_by_title(self):
    response = self.client.get(f"{self.list_url}?title=Harry Potter 1")
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(response.data), 1)

# Test Searching
def test_search_books(self):
    response = self.client.get(f"{self.list_url}?search=Rowling")
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(response.data), 2)

# Test Ordering
def test_order_books_by_year(self):
    response = self.client.get(f"{self.list_url}?ordering=-publication_year")
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data[0]['publication_year'], 1998)  # Most recent book first
