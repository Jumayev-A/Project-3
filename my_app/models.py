from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class CategoryModel(models.Model):
    user = models.ForeignKey(User, related_name='Auth', on_delete=models.CASCADE)
    name = models.CharField("Name", max_length=50)
    title = models.CharField("Title", max_length=50)
    file = models.FileField("File", upload_to='c_files/')



class BlogModel(models.Model):
    category = models.ForeignKey(CategoryModel, related_name='Category', on_delete=models.CASCADE)
    title = models.CharField("Title", max_length=50)
    description = models.TextField(default=None)
    file = models.FileField("File", upload_to='b_files/')

    def __str__(self):
        return self.title
    
    
    
