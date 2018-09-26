from django.db import models
from django.contrib.auth.models import User


class List(models.Model):
    name = models.CharField(max_length=255)


class Task(models.Model):
    name = models.CharField(max_length = 255)
    cr_date = models.DateTimeField()
    due_date = models.DateTimeField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    mark = models.BooleanField(default = False)
    list_id = models.ForeignKey(List, on_delete=models.CASCADE, default=None)