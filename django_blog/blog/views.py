from django.views.generic import CreateView, TemplateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, ProfileUpdateForm

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('profile')

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    form_class = ProfileUpdateForm
    template_name = 'profile_update.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user