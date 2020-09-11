from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView

from post.models import Post

from user.forms import CreatePost


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = UserCreationForm()
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')
        return render(request, 'register.html', {'form': form, "register": "active"})


def logIn(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        return render(request, 'login.html', {"login": "active"})


def home(request):
    blog_list = Post.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(blog_list, 10)
    try:
        blog_list = paginator.page(page)
    except PageNotAnInteger:
        blog_list = paginator.page(1)
    except EmptyPage:
        blog_list = paginator.page(paginator.num_pages)
    return render(request, 'home.html', {'blog_list': blog_list})


def logOut(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def newPost(request):
    if request.method == "POST":
        form = CreatePost(request.POST, request.FILES or None)
        # ctx = {'form': form}
        if form.is_valid():
            post = form.save()
            post.save()
            messages.info(request, 'Your post sending is success!')
    else:
        form = CreatePost()
    return render(request, 'create_post.html', {'form': form})
