from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from my_app.models import CategoryModel, BlogModel

# Create your views here.
def home(request):
    categories = CategoryModel.objects.all()
    context = {
        'categories':categories,
    }
    return render(request, 'home.html',context)

@login_required(login_url='/account/login/')
def create_category(request):
    user = request.user
    if request.method == 'POST':
        name = request.POST.get('name')
        title = request.POST.get('title')
        file = request.FILES.get('file')
        CategoryModel.objects.create(user=user, name=name, title=title, file=file).save()
        print(user)
        return redirect('my_app:home')
    return render(request, 'create_category.html',{})

def del_category(request, pk):
    CategoryModel.objects.get(id=pk).delete()
    messages.success(request, 'ustunlikli pozuldy ')
    return redirect('my_app:home')

@login_required(login_url='/account/login/')
def update_category(request, pk):
    model = CategoryModel.objects.get(id=pk)
    if request.method == 'POST':
        name = request.POST.get('name')
        title = request.POST.get('title')
        file = request.FILES.get('file')
        model = CategoryModel.objects.get(id=pk)
        model.name = name
        model.title = title
        model.file = file
        model.save()
        return redirect('my_app:home')
    return render(request, 'update_category.html',{'model':model})
def view_blog(request, pk):
    blogs = BlogModel.objects.filter(category_id=pk)
    return render(request, 'blog_list.html',{'blogs':blogs,'pk':pk})

@login_required(login_url='/account/login/')
def create_blog(request, pk):
    user = request.user
    if request.method == 'POST':
        category = CategoryModel.objects.get(id=pk)
        ct=category.name
        title = request.POST.get('title')
        description = request.POST.get('description')
        file = request.FILES.get('file')
        BlogModel.objects.create(category_id=pk, title=title, description=description, file=file).save()
        print(user)
        return redirect('my_app:blog_list',pk)
    return render(request, 'create_blog.html',{"pk":pk})
def del_blog(request, pk):
    model = BlogModel.objects.get(id=pk)
    model.delete()
    messages.success(request, 'ustunlikli pozuldy ')
    return redirect('my_app:blog_list', model.category_id)

@login_required(login_url='/account/login/')
def update_blog(request, pk):
    model = BlogModel.objects.get(id=pk)
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        file = request.FILES.get('file')
        model = BlogModel.objects.get(id=pk)
        model.title = title
        model.description = description
        model.file = file
        model.save()
        return redirect('my_app:blog_list', model.category_id)
    return render(request, 'update_blog.html',{'model':model})
def blog_detail(request, id):
    blog = BlogModel.objects.get(id=id)
    return render(request, 'blog_detail.html',{'blog':blog})
