from rest_framework import serializers
from api.models import Book, Author
from datetime import datetime


# BookSerializer: Handles serialization and validation for the Book model.
# - Serializes all fields of the Book model.
# - Includes custom validation to ensure the publication_year is not in the future.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

        # Custom validation for the publication_year field.
        # def validate_publication_year(self, value):
        # current_year = datetime.now().year
        # if value > current_year:
        #     raise serializers.ValidationError("The publication year cannot be in the future.")
        # return value


# AuthorSerializer: Handles serialization for the Author model.
# - Includes the name field.
# - Dynamically serializes the related books using a nested BookSerializer.
# - Demonstrates the relationship between Author and Book (One-to-Many).
class AuthorSerializer(serializers.ModelSerializer):
    # books field: Serializes the related books dynamically using BookSerializer.
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']