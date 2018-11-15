from django.db import models
from django.contrib.auth.models import User


class Advert(models.Model):
    title = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.IntegerField()
    number_of_views = models.IntegerField(default=0)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
