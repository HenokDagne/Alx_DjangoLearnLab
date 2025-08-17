# Django Blog CRUD Features

This project implements a simple blog application using Django, supporting full CRUD (Create, Read, Update, Delete) operations for blog posts.



## Features

- **List Posts**: View all blog posts at `/posts/`.
- **View Post Details**: See the full content of a post at `/posts/<int:pk>/`.
- **Create Post**: Authenticated users can create new posts at `/posts/new/`.
- **Edit Post**: Only the author of a post can edit it at `/posts/<int:pk>/edit/`.
- **Delete Post**: Only the author of a post can delete it at `/posts/<int:pk>/delete/`.

### Tagging System

- **Add Tags to Posts**: When creating or editing a post, use the "Tags" field to enter a comma-separated list of tags (e.g., `django, blog, python`). New tags will be created automatically if they do not exist.
- **View Tags**: Tags are displayed with each post in the list and detail views. Clicking a tag filters posts by that tag.

### Search Functionality

- **Search Bar**: Use the search bar at the top of the post list or search results page to find posts by title, content, or tags.
- **Tag Filtering**: Click any tag to view all posts associated with that tag.
- **Search Results**: Matching posts are displayed on the search results page, showing relevant titles, content snippets, and tags.

### Comment System

- **Add Comment**: Authenticated users can add comments to any blog post directly from the post detail page. Use the form at the bottom of the post detail view.
- **Edit Comment**: Only the author of a comment can edit their comment using `/posts/<post_id>/comments/<comment_id>/edit/`.
- **Delete Comment**: Only the author of a comment can delete their comment using `/posts/<post_id>/comments/<comment_id>/delete/`.
- **Comment Visibility**: All comments for a post are visible to any user viewing the post detail page.
- **Permissions**:
   - Only authenticated users can add comments.
   - Only the comment author can edit or delete their own comments.
   - Unauthorized users attempting to edit or delete comments will receive a 403 Forbidden response.

### Comment Data Handling

- The `Comment` model includes `post`, `author`, `content`, `created_at`, and `updated_at` fields.
- The author is automatically set to the logged-in user when creating a comment.

### Comment Navigation

- The post detail template displays all comments and provides edit/delete links for the comment author.
- The comment form is shown only to authenticated users.

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
