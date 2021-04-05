from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.views.generic.edit import DeleteView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from my_app.models import CategoryModel, BlogModel
from my_app.forms import BlogForm

# Create your views here.
def home(request):
    categories = CategoryModel.objects.all()
    context = {
                'categories':categories,
            }
    if request.method == 'POST':
        q = request.POST.get('q')
        if q:
            queryset = BlogModel.objects.filter(Q(title__icontains=q)  )
            context['q']=queryset
            print(context)
            if len(queryset) == 0:
                messages.success(request, 'tapylmady')
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

class CategoryDeleteView(DeleteView):
    model = CategoryModel
    success_url = reverse_lazy('my_app:home')

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
    page = request.GET.get('page', 1)
    blog = BlogModel.objects.filter(category_id=pk)
    paginator = Paginator(blog, 3)
    try:
        blogs = paginator.page(page)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    count_pag = paginator.page_range
    return render(request, 'blog_list.html',{'count_pag':count_pag,'blogs':blogs,'pk':pk})

@login_required(login_url='/account/login/')
def create_blog(request, pk):
    user = request.user
    form = BlogForm()
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save()
            form.category_id=pk
            form.save()
            return redirect('my_app:blog_list',pk)
    return render(request, 'create_blog.html',{"pk":pk, 'form':form})

class BlogDeleteView(DeleteView):
    model = BlogModel
    print(model)
    print(object)
    def get_success_url(self):
        return reverse('my_app:blog_list',args = {self.object.category_id})
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
