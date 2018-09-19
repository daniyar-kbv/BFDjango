from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

import datetime


def todo_list(request):
    tasks = [{
                'num': i,
                'cr_date': "10/09/2018",
                'due_date': "12/09/2018",
                'owner': "admin",
                'mark': False if i == 0 else True} for i in range(0, 5)]


    context = {
        'list':  tasks,
    }
    return render(request, 'todo_list.html', context)


def completed_todo_list(request):
    tasks = [{
                'num': i,
                'cr_date': "10/09/2018",
                'due_date': "12/09/2018",
                'owner': "admin",
                'mark': False if i == 0 else True} for i in range(0, 5)]
    context = {
        'list':  tasks,
    }
    return render(request, 'completed_todo_list.html', context)