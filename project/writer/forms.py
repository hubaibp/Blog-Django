from django import forms
from writer.models import BlogModel
from django.contrib.auth.models import User


class BlogWriteForm(forms.ModelForm):
  class Meta:
    model = BlogModel
    fields = ['title', 'blog', 'author_name', 'image']
    widgdgets = {
      'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title11'}),
      'blog': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write your blog here'}),
      'author_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Author Name'}),
      'image': forms.ClearableFileInput(attrs={'class': 'form-control custom-file-input', 'placeholder': 'Upload Image'}),
    }