from django.db import models
from datetime import datetime
from django.urls import reverse_lazy
from django.contrib.auth.models import User


class PostManager(models.Manager):
    def for_user(self, user):
        return self.filter(user=user)


class Post(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    cr_date = models.DateTimeField(default=datetime.now())
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    objects = PostManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('index')


class Comment(models.Model):
    cr_date = models.DateTimeField(default=datetime.now())
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    content = models.CharField(max_length=255)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, default=None)