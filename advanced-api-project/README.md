# API View Documentation for advanced_api_project

This project uses Django REST Framework generic views and mixins to efficiently handle CRUD operations for the Book model. Below is an overview of each view and its configuration:


## Filtering, Searching, and Ordering in BookListView

The `BookListView` uses Django REST Framework's built-in features to provide flexible querying:

- **Filtering:**
	- Users can filter books by `title`, `author`, and `publication_year` using query parameters.
	- Example: `/api/books/?title=SomeTitle&author=1&publication_year=2020`

- **Searching:**
	- Users can search for books by `title` or author's name using the `search` query parameter.
	- Example: `/api/books/?search=SomeTitle`

- **Ordering:**
	- Users can order results by `title`, `publication_year`, `author`, or `id` using the `ordering` query parameter.
	- Example: `/api/books/?ordering=title` or `/api/books/?ordering=-publication_year`

These features are enabled in `BookListView` using the following configuration:

```python
filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
filterset_fields = ['title', 'author', 'publication_year']
search_fields = ['title', 'author__name']
ordering_fields = ['title', 'publication_year', 'author', 'id']
ordering = ['title']
```

See code comments in `api/views.py` for further details and usage examples.

### BookDetailView
- **Purpose:** Retrieve details of a single book by primary key (`pk`).
- **Class:** `RetrieveAPIView`
- **Permissions:** No authentication required by default.

### BookCreateView
- **Purpose:** Create new Book instances.
- **Class:** `CreateAPIView`
- **Permissions:** Only authenticated users can create books (`IsAuthenticated`).
- **Filtering/Search:** Supports filtering by `title` and `author`, and searching by `title` and `author__name`.
- **Custom Hook:** `perform_create` method for additional validation or logic before saving.

### BookUpdateView
- **Purpose:** Update existing Book instances.
- **Class:** `UpdateAPIView`
- **Permissions:** Only authenticated users can update books (`IsAuthenticated`).
- **Filtering/Search:** Supports filtering by `title` and `author`, and searching by `title` and `author__name`.
- **Custom Hook:** `perform_update` method for additional validation or logic before saving.

### BookDeleteView
- **Purpose:** Delete Book instances.
- **Class:** `DestroyAPIView`
- **Permissions:** Only authenticated users can delete books (`IsAuthenticated`).

## Custom Settings & Hooks
- **Permissions:** Integrated using DRF's `permissions` module for authentication checks.
- **Filtering/Search:** Enabled using `DjangoFilterBackend` and `SearchFilter` for flexible querying.
- **Custom Hooks:** `perform_create` and `perform_update` methods allow for custom validation and logic during object creation and update.

## Usage
- Endpoints are defined in `api/urls.py` and are accessible under `/api/books/`, `/api/books/<int:pk>/`, etc.
- See code comments in `api/views.py` for further details on each view's configuration and behavior.

---
For more information, refer to the code comments in `api/views.py` and the Django REST Framework documentation.
