from .forms import CustomUserCreationForm, ProfileUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView  
from .models import User

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
    
