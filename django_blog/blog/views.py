from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView, UpdateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, ProfileUpdateForm

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile_template/profile.html'

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('profile')

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    form_class = ProfileUpdateForm
    template_name = 'profile_template/profile_update.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user
