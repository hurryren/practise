from django.shortcuts import render
from apps.blog.models import Article
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import Http404
from django.conf import settings

# Create your views here.


def home(request):  #zhuye
    posts = Article.objects.all()
    paginator = Paginator(posts, settings.PAGE_NUM)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)
    return render(request, 'home.html', {'post_list': post_list})


def detail(request,id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post': post})
