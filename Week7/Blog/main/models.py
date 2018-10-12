from django.db import models
from datetime import datetime


class Post(models.Model):
    author = models.CharField(max_length=255)
    cr_date = models.DateTimeField(default=datetime.now())
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)


class Comment(models.Model):
    cr_date = models.DateTimeField(default=datetime.now())
    author = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, default=None)