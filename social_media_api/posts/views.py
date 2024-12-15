from rest_framework import viewsets, permissions, filters, generics
from posts.models import Post, Comment
from posts.serializers import PostSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

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

    def get(self, request):
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
