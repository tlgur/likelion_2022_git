from distutils.command.upload import upload
from operator import length_hint
from tkinter import CASCADE
from django.db import models

class blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    photo = models.ImageField(blank=True, null = True, upload_to='blog_photo')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment