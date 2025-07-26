# Permission-protected book list view
from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import ExampleForm

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})
from django.shortcuts import render

# Create your views here.
