## Blog Post CRUD Features

This project supports full CRUD operations for blog posts.

### Features
- View all posts
- View a single post
- Create posts (authenticated users only)
- Edit posts (author only)
- Delete posts (author only)

### Permissions
- LoginRequiredMixin restricts creation
- UserPassesTestMixin ensures only authors can edit or delete posts

### Templates
Templates are located in blog/templates/blog/
