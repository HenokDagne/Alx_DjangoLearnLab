from rest_framework import mixins, generics
from .models import Book, Author
from .serializers import BookSerializer

# List all books & create new books
class BookListCreateView(mixins.ListModelMixin,
                         mixins.CreateModelMixin,
                         generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # GET -> list all
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    # POST -> create new
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# Retrieve, update, delete a book
class BookRetrieveUpdateDestroyView(mixins.RetrieveModelMixin,
                                    mixins.UpdateModelMixin,
                                    mixins.DestroyModelMixin,
                                    generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # GET -> retrieve
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    # PUT -> update full object
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    # PATCH -> partial update
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    # DELETE -> remove object
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



