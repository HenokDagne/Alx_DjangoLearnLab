from .forms import CustomUserCreationForm, ProfileUpdateForm, CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView  
from .models import User, Comment
from django.views.generic import ListView, DetailView, DeleteView
from .models import Post
from django.contrib.auth.mixins import UserPassesTestMixin

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    
class ProfileView(TemplateView):
    template_name = 'accounts/profile.html'
    
class ProfileUpdateView(UpdateView, LoginRequiredMixin):
    model = User
    form_class = ProfileUpdateForm
    success_url = reverse_lazy('profile')
    template_name = 'accounts/profile_update.html'
    
    def get_object(self):
        return self.request.user

# CRUD Views for Post
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'


from django.shortcuts import redirect
from django.views import View

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all().order_by('-created_at')
        context['comment_form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            comment = form.save(commit=False)
            comment.post = self.object
            comment.author = request.user
            comment.save()
            return redirect('post-detail', pk=self.object.pk)
        context = self.get_context_data()
        context['comment_form'] = form
        return self.render_to_response(context)
# ...existing code...

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def test_func(self):
        comment = self.get_object()
        return comment.author == self.request.user

    def get_success_url(self):
        return self.object.post.get_absolute_url() if hasattr(self.object.post, 'get_absolute_url') else f"/posts/{self.object.post.pk}/"

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'

    def test_func(self):
        comment = self.get_object()
        return comment.author == self.request.user

    def get_success_url(self):
        return self.object.post.get_absolute_url() if hasattr(self.object.post, 'get_absolute_url') else f"/posts/{self.object.post.pk}/"

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post-list')

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user
    
