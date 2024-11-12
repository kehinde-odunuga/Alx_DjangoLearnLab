from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from .views import list_books

urlpatterns = [
    path('list_books/', views.list_books),
    path('library/<int:pk>/', views.LibraryDetailView.as_view()),
    path('', views.homepage, name='homepage'),
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='user_login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='user_logout'),
    path('register/', views.register, name='register'),
]
