from django.contrib import admin
from my_app.models import CategoryModel, BlogModel
# Register your models here.


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    class Meta:
        model = CategoryModel
        fields = '__all__'


@admin.register(BlogModel)
class BlogModelAdmin(admin.ModelAdmin):
    class Meta:
        model = BlogModel
        fields = '__all__'
