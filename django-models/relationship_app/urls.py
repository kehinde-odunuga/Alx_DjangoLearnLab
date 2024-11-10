from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import list_books

urlpatterns = [
    path('list_books/', views.list_books),
    path('library/<int:pk>/', views.LibraryDetailView.as_view()),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),  # This should be present
]