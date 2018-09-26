from django.shortcuts import render
from .models import List, Task
from .forms import SearchForm


from django.http import HttpResponse

import datetime


def show_lists(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            search = form.cleaned_data['name']
            context = {
                'lists': List.objects.filter(name__contains=search),
                'form': form
            }
            return render(request, 'lists.html', context)
        if request.GET.get('order', '') != '':
            context = {
                'lists': List.objects.order_by('name')
            }
            return render(request, 'lists.html', context)
    context = {
        'lists': List.objects.all(),
    }
    return render(request, 'lists.html', context)


def todo_list(request, list):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            search = form.cleaned_data['name']
            tasks = Task.objects.filter(mark = False, list_id = list)
            context = {
                'tasks': tasks.filter(name__contains = search),
                'form': form
            }
            return render(request, './todo_list.html', context)
    if request.GET.get('order', '') != '':
        tasks = Task.objects.filter(mark = False, list_id=list)
        context = {
            'tasks': tasks.order_by(request.GET.get('order', ''))
        }
        return render(request, 'todo_list.html', context)
    tasks = Task.objects.filter(mark = False, list_id = list)
    context = {
        'tasks': tasks
    }

    return render(request, 'todo_list.html', context)


def completed_todo_list(request, list):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            search = form.cleaned_data['name']
            tasks = Task.objects.filter(mark = True, list_id = list)
            context = {
                'tasks': tasks.filter(name__contains = search),
                'form': form
            }
            return render(request, 'completed_todo_list.html', context)
    if request.GET.get('order', '') != '':
        tasks = Task.objects.filter(mark = True, list_id = list)
        context = {
            'tasks': tasks.order_by('name'),
        }
        return render(request, 'completed_todo_list.html', context)
    tasks = Task.objects.filter(mark = True, list_id = list)
    context = {
        'tasks': tasks,
    }
    return render(request, 'completed_todo_list.html', context)