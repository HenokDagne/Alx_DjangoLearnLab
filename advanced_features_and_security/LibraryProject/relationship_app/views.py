from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from .models import UserProfile
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required

def list_books(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
        model = Library
        template_name = 'relationship_app/library_detail.html'
        context_object_name = 'library'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['books'] = self.object.book_set.all()
            return context

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

@user_passes_test(lambda u: hasattr(u, 'profile') and u.profile.role == 'admin')
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(lambda u: hasattr(u, 'profile') and u.profile.role == 'librarian')
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(lambda u: hasattr(u, 'profile') and u.profile.role == 'member')
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        # Handle book creation logic
        pass
    return render(request, 'relationship_app/add_book.html')
@permission_required('relationship_app.can_change_book', raise_exception=True)
def change_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        # Handle book update logic
        pass
    return render(request, 'relationship_app/change_book.html', {'book': book})

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    if request.method ==  'POST':
        try:
            book = get_object_or_404(Book, id=book_id)
            book.delete()
            return redirect('list_books')
        except Book.DoesNotExist:
            return render(request, 'relationship_app/error.html', {'message': 'Book not found'})
    return render(request, 'relationship_app/delete_book.html', {'book_id': book_id})


