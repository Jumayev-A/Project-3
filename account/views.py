from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

def login_view(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user is not None:
            login(request, user)
            messages.success(request, 'Hello ')

            return redirect('my_app:home')
    context = {}
    return render(request, 'login.html', context)
def register_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password1')
        re_password = request.POST.get('password2')
        if len(password) > 0 and password == re_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists.')
            else:
                User.objects.create_user(first_name=first_name, last_name=last_name, username=username, password=password)
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Hello ')
                    return redirect('my_app:home')
        else:
            messages.error(request, 'Parol den dal.')
            return redirect('account:register')
    return render(request, 'register.html',{})

