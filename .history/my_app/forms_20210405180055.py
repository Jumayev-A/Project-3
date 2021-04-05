from django import forms 
from my_app.models import BlogModel

class BlogForm(forms.ModelForm):
    class Meta:
        db_table = ''
        managed = True
       
    model = BlogModel
    fields = []