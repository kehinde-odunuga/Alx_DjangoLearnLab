## Project Setup Files

### **Django Project Structure**
```
social_media_api/
|-- social_media_api/
|   |-- __init__.py
|   |-- settings.py
|   |-- urls.py
|   |-- wsgi.py
|   |-- asgi.py
|
|-- accounts/
|   |-- migrations/
|   |-- __init__.py
|   |-- admin.py
|   |-- apps.py
|   |-- models.py
|   |-- serializers.py
|   |-- views.py
|   |-- urls.py
|   |-- tests.py
|
|-- posts/
|   |-- migrations/
|   |-- __init__.py
|   |-- admin.py
|   |-- apps.py
|   |-- models.py
|   |-- serializers.py
|   |-- views.py
|   |-- urls.py
|   |-- tests.py
|
|-- manage.py
|
|-- db.sqlite3
|
|-- README.md
```

### **Initial Migrations**
Run these commands to create initial migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```


```markdown
# Advanced API Project - Accounts

### Setup Instructions
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Apply migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
4. Create a superuser for admin access:
   ```bash
   python manage.py createsuperuser
   ```
5. Run the development server:
   ```bash
   python manage.py runserver
   ```

### Endpoints

#### 1. Registration
- **URL**: `/accounts/register/`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
      "username": "testuser",
      "password": "password123",
      "password2": "password123",
      "email": "test@example.com",
      "bio": "This is a test bio."
  }
  ```
- **Response**:
  ```json
  {
      "message": "User registered successfully.",
      "token": "<auth-token>"
  }
  ```

#### 2. Login
- **URL**: `/accounts/login/`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
      "username": "testuser",
      "password": "password123"
  }
  ```
- **Response**:
  ```json
  {
      "message": "Login successful.",
      "token": "<auth-token>"
  }
  ```

#### 3. Profile Management
- **URL**: `/accounts/profile/`
- **Method**: `GET` or `PUT`
- **Authentication**: Token required
- **Response**:
  ```json
  {
      "username": "testuser",
      "email": "test@example.com",
      "bio": "This is a test bio.",
      "profile_picture": null,
      "followers": []
  }
  ```

#### 4. Posts
- **List Posts**: `GET /posts/`
- **Create Post**: `POST /posts/`
- **Retrieve Post**: `GET /posts/<id>/`
- **Update Post**: `PUT /posts/<id>/`
- **Delete Post**: `DELETE /posts/<id>/`

#### 5. Comments
- **List Comments**: `GET /comments/`
- **Create Comment**: `POST /comments/`
- **Retrieve Comment**: `GET /comments/<id>/`
- **Update Comment**: `PUT /comments/<id>/`
- **Delete Comment**: `DELETE /comments/<id>/`

### Search and Filter Examples
- Search Posts: `GET /posts/?search=keyword`
- Order Posts: `GET /posts/?ordering=-created_at`

### Follow Management
- **Follow a User**: `POST /api/accounts/follow/<user_id>/`
- **Unfollow a User**: `POST /api/accounts/unfollow/<user_id>/`

### Feed
- **User Feed**: `GET /api/posts/feed/`
  - Requires authentication.
  - Displays posts from users the authenticated user follows.
