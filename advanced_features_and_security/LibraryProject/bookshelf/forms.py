from django import forms
from .models import Book  # Replace with your actual model name

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author_name', 'published_date', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }

class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False, label='Search for books')
