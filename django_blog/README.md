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


## Comment System

### Features
- Add comments to blog posts.
- Edit or delete comments (only by the author).
- Display all comments under their respective posts.

### Permissions
- Only authenticated users can add, edit, or delete comments.
- All users can view comments.

### Usage
- Add a comment: `/post/<post_id>/comments/new/`
- Edit a comment: `/comments/<comment_id>/edit/`
- Delete a comment: `/comments/<comment_id>/delete/`
