from django.shortcuts import render
from django.http import HttpResponse
from post.models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from post.form import PostForm, PostImageForm
from django.views.generic.edit import CreateView, FormView


def index(request):
    blog_list = Post.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(blog_list, 10)
    try:
        blog_list = paginator.page(page)
    except PageNotAnInteger:
        blog_list = paginator.page(1)
    except EmptyPage:
        blog_list = paginator.page(paginator.num_pages)
    return render(request, 'index.html', {'blog_list': blog_list})


def post_detail(request, id):
    # id = request.GET.get('id')
    blog = Post.objects.filter(id=id)

    return render(request, 'post.html', {'blog': blog})


class BlogDownloadImageView(FormView):
    form_class = PostImageForm
    template_name = ''
