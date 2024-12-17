from rest_framework.routers import DefaultRouter
from django.urls import path, include
from posts.views import PostViewSet, CommentViewSet, FeedView

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
    path('posts/feed/<int:pk>/', FeedView.as_view(), name='feed'),
]