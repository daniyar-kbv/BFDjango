from django import forms
from .models import Restaurant, Dish


class RestForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ('name', 'number', 'telephone', 'city', 'user',)


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ('name', 'description', 'price', 'user')


