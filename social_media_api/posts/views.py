from rest_framework import viewsets, permissions, filters, generics, status
from posts.models import Post, Comment, Like
from posts.serializers import PostSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'content']
    ordering_fields = ['created_at', 'title']

    def create(self, request, *args, **kwargs):
        print("Received request data:", request.data)
        print("Request method:", request.method)
        print("User authenticated:", request.user.is_authenticated)
        return super().create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        print("Performing create with user:", self.request.user)
        serializer.save(author=self.request.user)
    

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class FeedView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        followed_users = request.user.following.all()
        posts = Post.objects.filter(author__in=followed_users).order_by('-created_at')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
    def get_queryset(self):
        
        # Get the current user
        user = self.request.user
        # Retrieve users the current user is following
        following_users = user.following.all()
        # Filter posts authored by those users
        return Post.objects.filter(author__in=following_users).order_by('-created_at')

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class LikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):

        post = get_object_or_404(Post, pk=pk)

        user = request.user
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response({"detail": "Post not found"}, status=status.HTTP_404_NOT_FOUND)

        # Check if user already liked the post
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if not created:
            return Response({"detail": "You already liked this post"}, status=status.HTTP_400_BAD_REQUEST)

        # Create a notification for the post's author
        Notification.objects.create(
            recipient=post.author,
            actor=user,
            verb="liked",
            target_content_type=ContentType.objects.get_for_model(post),
            target_object_id=post.id
        )

        return Response({"detail": "Post liked successfully"}, status=status.HTTP_201_CREATED)

class UnlikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):

        post = get_object_or_404(Post, pk=pk)

        user = request.user
        try:
            post = Post.objects.get(pk=pk)
            like = Like.objects.get(user=user, post=post)
            like.delete()
            return Response({"detail": "Post unliked successfully"}, status=status.HTTP_200_OK)
        except (Post.DoesNotExist, Like.DoesNotExist):
            return Response({"detail": "Like not found"}, status=status.HTTP_404_NOT_FOUND)
