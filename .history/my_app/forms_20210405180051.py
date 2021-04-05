from django import forms 
from my_app.models import BlogModel

class BlogForm(forms.ModelForm):
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'ModelName'
        verbose_name_plural = 'ModelNames'
    model = BlogModel
    fields = []