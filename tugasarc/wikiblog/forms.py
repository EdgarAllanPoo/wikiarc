from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta :
        model = Blog
        fields = [
            'title',
            'body',
        ]

class RawBlogForm(forms.Form):
    title = forms.CharField()
    body = forms.CharField()
