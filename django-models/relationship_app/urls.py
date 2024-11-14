from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from .views import list_books
from .views import LibraryDetailView

urlpatterns = [
    path('list_books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('', views.homepage, name='homepage'),
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='user_login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='user_logout'),
    path('register/', views.register, name='register'),
    path('admin_view/', views.admin_view, name='admin_view'),
    path('librarian_view/', views.librarian_view, name='librarian_view'),
    path('member_view/', views.member_view, name='member_view'),
]
