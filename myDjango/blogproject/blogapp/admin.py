from xml.etree.ElementTree import Comment
from django.contrib import admin
from .models import blog, Comment

admin.site.register(blog)
admin.site.register(Comment)