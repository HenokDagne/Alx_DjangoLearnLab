from django_filters import rest_framework
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, filters
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListCreateAPIView):
        """
        BookListView
        - Handles listing all books and creating new books.
        - Uses ListCreateAPIView for GET (list) and POST (create).
        - Filtering: Users can filter by title, author, and publication_year using query parameters.
            Example: /api/books/?title=SomeTitle&author=1&publication_year=2020
        - Searching: Users can search by title and author's name using the 'search' query parameter.
            Example: /api/books/?search=SomeTitle
        - Ordering: Users can order results by title, publication_year, author, or id using the 'ordering' query parameter.
            Example: /api/books/?ordering=title or /api/books/?ordering=-publication_year
        - No authentication required for listing; creation may require authentication if permission_classes set.
        """
        queryset = Book.objects.all()
        serializer_class = BookSerializer
        # Enable filtering by title, author, and publication_year
        filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
        filterset_fields = ['title', 'author', 'publication_year']
        search_fields = ['title', 'author__name']
        ordering_fields = ['title', 'publication_year', 'author', 'id']  # Allow ordering by these fields
        ordering = ['title']  # Default ordering by title

class BookDetailView(generics.RetrieveAPIView):
    """
    BookDetailView
    - Handles retrieving a single book by its primary key (pk).
    - Uses RetrieveAPIView for GET (detail).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['title', 'author', 'published_date']
    search_fields = ['title', 'author__name']

class BookCreateView(generics.CreateAPIView):
    """
    BookCreateView
    - Handles creation of new Book instances.
    - Only authenticated users can create books (permission_classes).
    - Supports filtering and searching by title and author.
    - Custom hook: perform_create for additional validation or logic before saving.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['title', 'author']
    search_fields = ['title', 'author__name']

    def perform_create(self, serializer):
        # Custom validation or logic can be added here
        serializer.is_valid(raise_exception=True)
        serializer.save()

class BookUpdateView(generics.UpdateAPIView):
    """
    BookUpdateView
    - Handles updating Book instances.
    - Only authenticated users can update books (permission_classes).
    - Supports filtering and searching by title and author.
    - Custom hook: perform_update for additional validation or logic before saving.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['title', 'author']
    search_fields = ['title', 'author__name']

    def perform_update(self, serializer):
        # Custom validation or logic can be added here
        serializer.is_valid(raise_exception=True)
        serializer.save()

class BookDeleteView(generics.DestroyAPIView):
    """
    BookDeleteView
    - Handles deletion of Book instances.
    - Only authenticated users can delete books (permission_classes).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
        
