from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from .models import Post

User = get_user_model()

class PostAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_create_post(self):
        data = {"title": "Test Post", "content": "This is a test post."}
        response = self.client.post("/posts/", data)
        self.assertEqual(response.status_code, 201)

    def test_list_posts(self):
        Post.objects.create(author=self.user, title="Test Post", content="Test Content")
        response = self.client.get("/posts/")
        self.assertEqual(response.status_code, 200)
