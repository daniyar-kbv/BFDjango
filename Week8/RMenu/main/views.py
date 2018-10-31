from django.shortcuts import render, redirect
from .models import Restaurant, Dish, DishReview, RestReview, City
from .forms import RestForm, DishForm
from django.contrib.auth.models import User
from django.views import View
from django.views.generic.edit import UpdateView


class HomeView(View):
    def get(self, request):
        context = {
            'rests': Restaurant.objects.all()
        }
        return render(request, 'main/rests.html', context)


class CreateRestView(View):
    def get(self, request):
        form = RestForm()
        context = {
            'form': form,
            'users': User.objects.all(),
            'cities': City.objects.all()
        }
        return render(request, 'main/create_rest.html', context)

    def post(self, request):
        form = RestForm(request.POST)
        if form.is_valid():
            print("not valid:(")
            form.save()
            return redirect('./')


class DeleteRestView(View):
    def get(self, request, fk):
        model = Restaurant.objects.get(pk=fk)
        model.delete()
        return redirect('..')


class UpdateRestView(View):
    def get(self, request, fk):
        form = RestForm()
        context = {
            'form': form,
            'rest': Restaurant.objects.get(pk=fk),
            'users': User.objects.all(),
            'cities': City.objects.all()
        }
        return render(request, 'main/update_rest.html', context)

    def post(self, request, fk):
        form = RestForm(request.POST)
        if form.is_valid():
            rest = Restaurant.objects.get(pk=fk)
            rest.name = form.cleaned_data['name']
            rest.number = form.cleaned_data['number']
            rest.telephone = form.cleaned_data['telephone']
            rest.user = form.cleaned_data['user']
            rest.city = form.cleaned_data['city']
            rest.save()
            return redirect('..')


# class RestUpdate(UpdateView):
#     model = Restaurant
#     fields = ['name', 'number', 'telephone', 'city', 'user']
#     template_name_suffix = '_update_form'


class RestInfo(View):
    def get(self, request, fk):
        context = {
            'rest': Restaurant.objects.get(pk=fk),
            'reviews': RestReview.objects.filter(restaurant = Restaurant.objects.get(pk=fk))
        }
        return render(request, 'main/rest_info.html', context)


class CreateRestReview(View):
    def get(self, request):
        form = RestForm()
        context = {
            'form': form,
            'users': User.objects.all(),
            'cities': City.objects.all()
        }
        return render(request, 'main/create_rest.html', context)

    def post(self, request):
        form = RestForm(request.POST)
        if form.is_valid():
            print("not valid:(")
            form.save()
            return redirect('./')

class DishesView(View):
    def get(self, request, fk):
        context = {
            'dishes': Dish.objects.filter(pk=fk)
        }
        return render(request, 'main/dishes.html', context)


class CreateDishView(View):
    def get(self, request, fk):
        form = DishForm()
        context = {
            'form': form,
            'users': User.objects.all()
        }
        return render(request, 'main/create_dish.html', context)

    def post(self, request, fk):
        form = DishForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            user = form.cleaned_data['user']
            dish = Dish()
            dish.name = name
            dish.description = description
            dish.price = price
            dish.user = user
            dish.restaurant = Restaurant.objects.get(pk=fk)
            dish.save()
            return redirect('../')

