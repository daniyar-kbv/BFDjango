from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class City(models.Model):
    name = models.CharField(max_length=255)


class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    number = models.IntegerField()
    telephone = models.IntegerField()
    city = models.ForeignKey(City, on_delete=models.SET_DEFAULT, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Dish(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)


class RestRewiew(models.Model):
    rating = models.IntegerField()
    comment = models.CharField(max_length=255)
    date = models.DateTimeField(default=datetime.now())
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)


class DishReview(models.Model):
    rating = models.IntegerField()
    comment = models.CharField(max_length=255)
    date = models.DateTimeField(default=datetime.now())
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
