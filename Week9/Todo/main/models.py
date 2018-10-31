from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy


class Manager(models.Manager):
    def for_user(self, user):
        return self.filter(user=user)


class List(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    objects = Manager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('index')


class Task(models.Model):
    name = models.CharField(max_length = 255)
    cr_date = models.DateTimeField()
    due_date = models.DateTimeField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    mark = models.BooleanField(default = False)
    list_id = models.ForeignKey(List, on_delete=models.CASCADE, default=None)