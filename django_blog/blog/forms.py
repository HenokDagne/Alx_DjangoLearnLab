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

# Form for Comment model
class CommentForm(forms.ModelForm):
    class Meta:
        model = Post.comments.rel.related_model
        fields = ['content']

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if not content or not content.strip():
            raise forms.ValidationError('Comment cannot be empty.')
        return content
        