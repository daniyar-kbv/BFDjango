from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import CommentForm, PostForm
from django.utils.dateparse import parse_datetime
from datetime import datetime
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.models import User


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView, LoginRequiredMixin):
    model = Post
    fields = ['title', 'content']
    success_url = reverse_lazy('blog')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog')

    def get_queryset(self):
        return Post.objects.for_user(user=self.request.user)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    success_url = reverse_lazy('blog')

    def get_queryset(self):
        return Post.objects.for_user(user=self.request.user)


class CreateCommentView(View):
    def get(self, request, fk):
        form = CommentForm()
        context = {
            'form': form
        }
        return render(request, 'main/create_comment.html', context)

    def post(self, request, fk):
        form = CommentForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            user = form.cleaned_data['user']
            comment = Comment()
            comment.user = user
            comment.content = content
            comment.post_id = Post.objects.get(pk=fk)
            comment.save()
            return redirect('./post')


class CommentDeleteView(View):
    def get(self, request, comment, fk):
        del_list = Comment.objects.get(pk=comment)
        del_list.delete()
        return redirect('../post')


class CommentUpdateView(View):
    def get(self, request, fk, comment):
        form = CommentForm()
        context = {
            'form': form,
            'comment': Comment.objects.get(pk=comment)
        }
        return render(request, 'main/update_comment.html', context)

    def post(self, request, fk, comment):
        form = CommentForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            comment = Comment.objects.get(pk=comment)
            comment.user = form.cleaned_data['user']
            comment.content = form.cleaned_data['content']
            comment.save()
            return redirect('../post')