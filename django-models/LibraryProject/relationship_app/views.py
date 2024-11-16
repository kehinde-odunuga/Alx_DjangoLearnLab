from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse, HttpResponseForbidden
from django.views.generic import TemplateView, ListView, UpdateView
from django.views.generic.detail import DetailView
from .models import Library, Book, UserProfile
from .utils import is_admin, is_librarian, is_member
from .forms import BookForm
from django.http import Http404


#Create your views here.

def homepage(request):
    return HttpResponse('homepage')


def about(request):
    return HttpResponse('about')


def hello_view(request):
    """A basic function view returning a greeting message."""
    return HttpResponse("Hello, World!")

# books
def list_books(request):
    """Retrieves all books and renders a template displaying the list."""
    books = Book.objects.all()  # Fetch all book instances from the database
    context = {'books': books}  # Create a context dictionary with book list
    return render(request, 'relationship_app/list_books.html', context)

def book_list(request):
    books = Book.objects.all()  # Query all books
    return render(request, 'bookshelf/book_list.html', {'books': books})
LibraryProject/bookshelf/views.py doesn't contain: ["book_list", "books"]

# View for adding a book
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Redirect to the book list after successful creation
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})

# View for editing a book
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'edit_book.html', {'form': form})

# View for deleting a book
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'delete_book.html', {'book': book})


class HelloView(TemplateView):
    """A class-based view rendering a template named 'hello.html'."""
    template_name = 'hello.html'


class LibraryDetailView(DetailView):
    """A class-based view for displaying details of a list of books in a library."""
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
    
# User Registration View
def register(request):
    form = UserCreationForm()
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            
    context = {'form': form}
    return render(request, 'relationship_app/register.html', context)

# User Login View
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('homepage')  # Redirect to a home page or dashboard
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})


# User roles
def is_admin(user):
    return getattr(user, 'userprofile', None) and user.userprofile.role == 'Admin'

def is_librarian(user):
    return getattr(user, 'userprofile', None) and user.userprofile.role == 'Librarian'

def is_member(user):
    return getattr(user, 'userprofile', None) and user.userprofile.role == 'Member'

# Views for each role
@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
