from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import CommentForm, PostForm
from django.utils.dateparse import parse_datetime
from datetime import datetime


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


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('./')
    else:
        form = PostForm()
    context = {
        'form': form
    }
    return render(request, 'create_post.html', context)


def delete_post(request, post):
    del_list = Post.objects.get(pk=post)
    del_list.delete()
    return redirect('..')


def update_post(request, post):
    if request.method == 'POST':
        form = PostForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            post = Post.objects.get(pk=post)
            post.author = form.cleaned_data['author']
            post.title = form.cleaned_data['title']
            post.content = form.cleaned_data['content']
            post.save()
            return redirect('..')
    else:
        form = PostForm()
    context = {
        'form': form,
        'post': Post.objects.get(pk=post)
    }
    return render(request, 'update_post.html', context)


def create_comment(request, post):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            author = form.cleaned_data['author']
            comment = Comment()
            comment.author = author
            comment.content = content
            comment.post_id = Post.objects.get(pk=post)
            comment.save()
            return redirect('./post')
    else:
        form = CommentForm()
    context = {
        'form': form
    }
    return render(request, 'create_comment.html', context)


def delete_comment(request, comment, post):
    del_list = Comment.objects.get(pk=comment)
    del_list.delete()
    return redirect('../post')

def update_comment(request, post, comment):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            comment = Comment.objects.get(pk=comment)
            comment.author = form.cleaned_data['author']
            comment.content = form.cleaned_data['content']
            comment.save()
            return redirect('../post')
    else:
        form = CommentForm()
    context = {
        'form': form,
        'comment': Comment.objects.get(pk=comment)
    }
    return render(request, 'update_comment.html', context)