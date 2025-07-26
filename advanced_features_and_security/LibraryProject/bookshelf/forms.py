from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']
        widgets = {
            'title': forms.TextInput(attrs={'required': True}),
            'author': forms.TextInput(attrs={'required': True}),
            'publication_year': forms.NumberInput(attrs={'min': 0}),
        }

    # Additional validation can be added here
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title:
            raise forms.ValidationError('Title is required.')
        return title
