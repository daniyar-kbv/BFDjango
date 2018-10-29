from django.shortcuts import render, redirect
from .models import Restaurant, Dish, DishReview, RestRewiew
from .forms import RestForm
from django.contrib.auth.models import User


def show_rests(request):
    if request.method == 'GET':
        context = {
            'rests': Restaurant.objects.all()
        }
        return render(request, 'main/rests.html', context)


def show_dishes(request, fk):
    if request.method == 'GET':
        context = {
            'dishes': Dish.objects.filter(pk=fk)
        }
        return render(request, 'main/dishes.html', context)


def create_rest(request):
    if request.method == 'POST':
        form = RestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('./')
    else:
        form = RestForm()

        context = {
            'form': form
        }
        return render(request, 'main/create_rest.html', context)