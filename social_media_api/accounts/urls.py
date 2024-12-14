from django.urls import path
from accounts.views import UserRegistrationView, UserLoginView, UserProfileView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
]
