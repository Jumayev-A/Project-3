from django import forms 
from my_app.models import BlogModel

class BlogForm(forms.ModelForm):
    model = BlogMode