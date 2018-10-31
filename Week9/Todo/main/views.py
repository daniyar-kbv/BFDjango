from django.shortcuts import render, redirect
from .models import List, Task
from .forms import SearchForm, ListForm
from django.views import View
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.models import User


class ListsView(View):
    def get(self, request):
        form = SearchForm(request.GET)
        if form.is_valid():
            search = form.cleaned_data['name']
            context = {
                'lists': List.objects.filter(name__contains=search),
                'form': form
            }
            return render(request, 'main/lists.html', context)
        if request.GET.get('order', '') != '':
            context = {
                'lists': List.objects.order_by('name')
            }
            return render(request, 'main/lists.html', context)
        context = {
            'lists': List.objects.all(),
        }
        return render(request, 'main/lists.html', context)


class TodoListView(View):
    def get(self, request, list):
        form = SearchForm(request.GET)
        if form.is_valid():
            search = form.cleaned_data['name']
            tasks = Task.objects.filter(mark = False, list_id = list)
            context = {
                'tasks': tasks.filter(name__contains = search),
                'form': form
            }
            return render(request, './main/todo_list.html', context)
        if request.GET.get('order', '') != '':
            tasks = Task.objects.filter(mark = False, list_id=list)
            context = {
                'tasks': tasks.order_by(request.GET.get('order', ''))
            }
            return render(request, 'main/todo_list.html', context)
        if request.POST.get('done_id', '') != '':
            task = Task.objects.get(id = 'done_id')
            task.mark = True
            task.save()
            return redirect('../todo_list')
        tasks = Task.objects.filter(mark = False, list_id = list)
        context = {
            'tasks': tasks
        }

        return render(request, 'main/todo_list.html', context)


class CompTodoListView(View):
    def get(self, request, list):
        form = SearchForm(request.GET)
        if form.is_valid():
            search = form.cleaned_data['name']
            tasks = Task.objects.filter(mark = True, list_id = list)
            context = {
                'tasks': tasks.filter(name__contains = search),
                'form': form
            }
            return render(request, 'main/completed_todo_list.html', context)
        if request.GET.get('order', '') != '':
            tasks = Task.objects.filter(mark = True, list_id = list)
            context = {
                'tasks': tasks.order_by('name'),
            }
            return render(request, 'main/completed_todo_list.html', context)
        tasks = Task.objects.filter(mark = True, list_id = list)
        context = {
            'tasks': tasks,
        }
        return render(request, 'main/completed_todo_list.html', context)


class CreateListView(CreateView, LoginRequiredMixin):
    model = List
    fields = ['name', 'user']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)


class MakeDoneView(View):
    def get(self, request, fk, pk):
        task = Task.objects.get(pk=pk)
        task.mark = True
        task.save()
        return redirect('../todo')


class MakeNotDoneView(View):
    def get(self, request, fk, pk):
        task = Task.objects.get(pk=pk)
        task.mark = False
        task.save()
        return redirect('../todo')


class DeleteListView(View):
    def get(self, request, fk):
        del_list = List.objects.get(pk=fk)
        del_list.delete()
        return redirect('..')