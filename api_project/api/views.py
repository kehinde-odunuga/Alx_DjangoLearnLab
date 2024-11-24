from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for handling CRUD operations for the Book model.
    """
    queryset = Book.objects.all()  # Fetch all Book objects
    serializer_class = BookSerializer  # Use BookSerializer for serialization
    permission_classes = [IsAuthenticated]

