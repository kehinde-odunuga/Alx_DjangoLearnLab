from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse, HttpResponseForbidden
from django.views.generic import TemplateView, ListView, UpdateView
from django.views.generic.detail import DetailView
from .models import Library
from .models import Book
from .utils import is_admin, is_librarian, is_member

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

# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('home')  # Replace 'home' with the desired redirect page after registration
#     else:
#         form = UserCreationForm()
#     return render(request, 'relationship_app/register.html', {'form': form})

# User Registration View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.save()
            login(request, user)
            # After successful registration, log the user in
            # username = form.cleaned_data.get('username')
            # password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=password)
            # login(request, user)
            return redirect('homepage')  # Redirect to a home page or dashboard
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

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

# User Logout View
@login_required
def user_logout(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')


@user_passes_test(is_admin)
def admin_view(request):
    context = {
        'role': 'Admin',
        'user': request.user
    }
    return render(request, 'roles/admin_dashboard.html', context)

@user_passes_test(is_librarian)
def librarian_view(request):
    context = {
        'role': 'Librarian',
        'user': request.user
    }
    return render(request, 'roles/librarian_dashboard.html', context)

@user_passes_test(is_member)
def member_view(request):
    context = {
        'role': 'Member',
        'user': request.user
    }
    return render(request, 'roles/member_dashboard.html', context)