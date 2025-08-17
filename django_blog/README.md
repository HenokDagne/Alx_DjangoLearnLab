# Django Blog CRUD Features

This project implements a simple blog application using Django, supporting full CRUD (Create, Read, Update, Delete) operations for blog posts.

## Features

- **List Posts**: View all blog posts at `/posts/`.
- **View Post Details**: See the full content of a post at `/posts/<int:pk>/`.
- **Create Post**: Authenticated users can create new posts at `/posts/new/`.
- **Edit Post**: Only the author of a post can edit it at `/posts/<int:pk>/edit/`.
- **Delete Post**: Only the author of a post can delete it at `/posts/<int:pk>/delete/`.

## Permissions

- **Authenticated Users**: Required for creating, editing, and deleting posts.
- **Post Author**: Only the author can edit or delete their own posts.
- **All Users**: Can view the list and details of posts.

## Data Handling

- The `Post` model includes `title`, `content`, `published_date`, and `author` fields.
- The author is automatically set to the logged-in user when creating a post.

## Navigation

- Templates include navigation links for creating, editing, deleting, and returning to the post list.

## Testing

- Automated tests are provided in `blog/tests.py` to verify CRUD functionality, permissions, and navigation.
- Run tests with:
  ```
  python manage.py test blog
  ```

## Setup

1. Install dependencies:
   ```
   pip install django
   ```
2. Run migrations:
   ```
   python manage.py migrate
   ```
3. Start the development server:
   ```
   python manage.py runserver
   ```

## Special Notes

- Ensure users are authenticated to create, edit, or delete posts.
- Unauthorized users attempting to edit or delete posts will receive a 403 Forbidden response.
- All templates are located in `templates/blog/` and are styled with the provided CSS.

---

For further customization or questions, see code comments or contact the project maintainer.
