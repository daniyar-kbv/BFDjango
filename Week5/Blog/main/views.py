from django.shortcuts import render
from .models import Post, Comment


def show_posts(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'posts.html', context)


def post_more(request, post):
    comments = Comment.objects.filter(post_id = post)
    post = Post.objects.get(id = post)
    context = {
        'post': post,
        'comments': comments
    }
    return render(request, 'post_more.html', context)