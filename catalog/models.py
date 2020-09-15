from datetime import datetime
from django.contrib.auth.models import User
from django.db import models


class Publication(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateTimeField("date published", default=datetime.now)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_modified = models.DateTimeField(auto_now=True, null=True)
    content = models.TextField()
    author = models.ForeignKey(User, verbose_name=u'автор поста', blank=True, null=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', null=True, blank=True)


class Message(models.Model):
    user_name = models.CharField(max_length=50)
    user_phone = models.CharField(max_length=200)
    user_text = models.TextField()


class CommentsPublication(models.Model):
    comment_name = models.CharField(max_length=50)
    comment_text = models.CharField(max_length=200)

