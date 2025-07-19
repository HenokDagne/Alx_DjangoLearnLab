from django.shortcuts import render
from relationship_app.models import Author, Book, Library, Librarian
from django.views.generic.detail import DetailView

# Create your views here.

def list_books(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'book_list.html', context)

class LibraryDetailView(DetailView):
        model = Library
        template_name = 'library_detail.html'
        context_object_name = 'library'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['books'] = self.object.book_set.all()
            return context
        
        
