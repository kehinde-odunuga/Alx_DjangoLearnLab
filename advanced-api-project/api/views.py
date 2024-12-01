from rest_framework import generics
from rest_framework.exceptions import ValidationError
from api.models import Book
from api.serializers import BookSerializer
from datetime import datetime
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

# ListView: Retrieve all books.
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'author__name']  # Enable search by title or author name


# DetailView: Retrieve a single book by ID.
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

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
