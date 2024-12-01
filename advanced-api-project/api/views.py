from rest_framework import generics
from rest_framework.exceptions import ValidationError
from api.models import Book
from api.serializers import BookSerializer
from datetime import datetime
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny

# ListView: Retrieve all books.
class BookListView(generics.ListAPIView):
    """
    List all books with advanced query capabilities:
    - Filtering: Filter books by title, author, or publication year.
    - Searching: Search books by title or author's name.
    - Ordering: Order results by title or publication year.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # filter_backends = [SearchFilter]
    permission_classes = [AllowAny]  # Publicly accessible
    filter_backends = [DjangoFilterBackend, SearchFilter]  # Add SearchFilter
    filterset_fields = ['title', 'author', 'publication_year']
    search_fields = ['title', 'author__name']  # Enable search by title or author name
    ordering_fields = ['title', 'publication_year']  # Allow ordering by these fields
    ordering = ['title']  # Default ordering



# DetailView: Retrieve a single book by ID.
class BookDetailView(generics.RetrieveAPIView):
    """
    Retrieve details of a specific book. Allows read-only access for all users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]  # Publicly accessible

# CreateView: Add a new book.
class BookCreateView(generics.CreateAPIView):
    """
    Handles the creation of a new book.
    Includes custom validation and permission checks.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can create a book

    def perform_create(self, serializer):
        # Additional validation logic
        title = serializer.validated_data.get('title')
        if Book.objects.filter(title=title).exists():
            raise ValidationError({"title": "A book with this title already exists."})
        serializer.save()

# UpdateView: Modify an existing book.
class BookUpdateView(generics.UpdateAPIView):
    """
    Handles the updating of an existing book.
    Includes custom validation and permission checks.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Authenticated users can update; others can only read

    def perform_update(self, serializer):
        # Additional validation logic before saving
        publication_year = serializer.validated_data.get('publication_year')
        if publication_year > datetime.now().year:  # Example of a custom rule
            raise ValidationError({"publication_year": "The year is too far in the future."})
        serializer.save()

# DeleteView: Remove a book.
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrReadOnly(BasePermission):
    """
    Custom permission: Admins have full access, others have read-only access.
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:  # GET, HEAD, OPTIONS
            return True
        return request.user and request.user.is_staff  # Only admins can modify



"""
API Query Capabilities:

1. Filtering:
   - Filter books by specific fields (e.g., title, author, publication_year).
   - Example: `/api/books/?title=The Great Gatsby`

2. Searching:
   - Perform text searches across specified fields.
   - Example: `/api/books/?search=Fitzgerald`

3. Ordering:
   - Sort results by specific fields.
   - Example: `/api/books/?ordering=publication_year` (ascending)
             `/api/books/?ordering=-publication_year` (descending)

Integrated DRF Features:
- DjangoFilterBackend for filtering.
- SearchFilter for full-text search.
- OrderingFilter for result sorting.
"""
