from django.urls import path
from . import views
from .views import list_books

urlpatterns = [
    path('list_books/', views.list_books),
    path('library/<int:pk>/', views.LibraryDetailView.as_view()),
]
