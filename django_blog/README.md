## Blog Post Management

### Features
- View a list of blog posts.
- View details of a single post.
- Create new blog posts (authenticated users only).
- Edit or delete your own posts.

### Setup
1. Run migrations: `python manage.py migrate`.
2. Start the server: `python manage.py runserver`.

### Permissions
- Only the author can edit or delete their posts.
- Unauthenticated users can only view posts.

### Navigation
- Home: `/`
- Create Post: `/post/new/`
