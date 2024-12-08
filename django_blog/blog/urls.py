from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from blog import views
from django.urls import path

urlpatterns = [
    # Built-in auth views
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Custom view for register and profile
    path('', views.home, name='home'),
    path('posts/', views.posts, name='posts'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='profile'),
]