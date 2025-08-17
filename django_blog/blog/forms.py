from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Post

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "bio")
        
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["email", "bio"]


# Form for Post model
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        