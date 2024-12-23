from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Book,  BookForm, SearchForm

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required

from django.http import HttpResponse, HttpResponseForbidden
from django.views.generic import TemplateView, ListView, UpdateView
from django.views.generic.detail import DetailView
from .models import Library, Book, UserProfile
from .utils import is_admin, is_librarian, is_member
from .forms import BookForm
from django.http import Http404

# Create your views here.

@permission_required('your_app_name.can_view', raise_exception=True)
def view_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'view_post.html', {'post': post})

@permission_required('your_app_name.can_create', raise_exception=True)
def create_post(request):
    if request.method == 'POST':
        # Handle post creation
        pass
    return render(request, 'create_post.html')

@permission_required('your_app_name.can_edit', raise_exception=True)
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        # Handle post editing
        pass
    return render(request, 'edit_post.html', {'post': post})

@permission_required('your_app_name.can_delete', raise_exception=True)
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.delete()
    return render(request, 'delete_post.html')


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

# book(bookshelf)
def book_list(request):
    books = Book.objects.all()  # Query all books
    return render(request, 'bookshelf/book_list.html', {'books': books})

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



def book_create_view(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Replace with your actual view name
    else:
        form = BookForm()
    return render(request, 'bookshelf/book_form.html', {'form': form})

def search_books_view(request):
    form = SearchForm(request.GET or None)
    books = Book.objects.none()
    if form.is_valid():
        query = form.cleaned_data['query']
        books = Book.objects.filter(title__icontains=query)
    return render(request, 'bookshelf/search_results.html', {'form': form, 'books': books})


from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import ExampleForm, SearchForm

def book_create_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Replace with your actual view name
    else:
        form = ExampleForm()
    return render(request, 'bookshelf/book_form.html', {'form': form})

def search_books_view(request):
    form = SearchForm(request.GET or None)
    books = Book.objects.none()
    if form.is_valid():
        query = form.cleaned_data['query']
        books = Book.objects.filter(title__icontains=query)
    return render(request, 'bookshelf/search_results.html', {'form': form, 'books': books})
