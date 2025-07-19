from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect


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
