from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from .models import Book, Library

# Create your views here.


def homepage(request):
    return HttpResponse('homepage')


def about(request):
    return HttpResponse('about')


def hello_view(request):
    """A basic function view returning a greeting message."""
    return HttpResponse("Hello, World!")


def list_books(request):
    """Retrieves all books and renders a template displaying the list."""
    books = Book.objects.all()  # Fetch all book instances from the database
    context = {'books': books}  # Create a context dictionary with book list
    return render(request, 'relationship_app/list_books.html', context)


class HelloView(TemplateView):
    """A class-based view rendering a template named 'hello.html'."""
    template_name = 'hello.html'


class LibraryDetailView(DetailView):
    """A class-based view for displaying details of a list of books in a library."""
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    # def get_context_data(self, **kwargs):
    #     """Injects additional context data specific to the library."""
    #     context = super().get_context_data(**kwargs)  # Get default context data
    #     library = self.get_object()  # Retrieve the current book instance
    #     context['average_rating'] = library.get_average_rating()
