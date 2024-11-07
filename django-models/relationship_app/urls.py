from django.urls import path
from . import views

urlpatterns = [
    path('list_books/', views.list_books),
    path('library/<int:pk>/', views.LibraryDetailView.as_view()),
]
