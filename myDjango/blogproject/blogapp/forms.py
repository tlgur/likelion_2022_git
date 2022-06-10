from dataclasses import fields
from tkinter import Widget
from xml.etree.ElementTree import Comment
from django import forms
from .models import blog, Comment

class BlogForm(forms.Form):
    title = forms.CharField()
    body = forms.CharField(widget=forms.Textarea)

class BlogModelForm(forms.ModelForm):
    class Meta:
        model = blog
        fields = '__all__'
        # fields = ['title', 'body']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']