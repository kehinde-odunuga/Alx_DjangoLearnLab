from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.viewsets import ModelViewSet

# Create your views here.

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(ModelViewSet):
    """
    A ViewSet for handling CRUD operations for the Book model.
    """
    queryset = Book.objects.all()  # Fetch all Book objects
    serializer_class = BookSerializer  # Use BookSerializer for serialization

