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
    tags = forms.CharField(required=False, help_text="Comma-separated list of tags.")

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['tags'].initial = ', '.join([tag.name for tag in self.instance.tags.all()])

    def save(self, commit=True):
        instance = super().save(commit=False)
        tags_str = self.cleaned_data.get('tags', '')
        tag_names = [name.strip() for name in tags_str.split(',') if name.strip()]
        if commit:
            instance.save()
            # Assign tags
            from .models import Tag
            tags = []
            for name in tag_names:
                tag, created = Tag.objects.get_or_create(name=name)
                tags.append(tag)
            instance.tags.set(tags)
        return instance

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
        