from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, filters
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Only authenticated users can create books
    permission_classes = [permissions.IsAuthenticated]
    # Enable filtering by title and author
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['title', 'author']
    search_fields = ['title', 'author__name']

    def perform_create(self, serializer):
        # Custom validation or logic can be added here
        serializer.is_valid(raise_exception=True)
        serializer.save()

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Only authenticated users can update books
    permission_classes = [permissions.IsAuthenticated]
    # Enable filtering and searching
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['title', 'author']
    search_fields = ['title', 'author__name']

    def perform_update(self, serializer):
        # Custom validation or logic can be added here
        serializer.is_valid(raise_exception=True)
        serializer.save()

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
        
