from django import views
from django.urls import path
from polls import views

urlpatterns = [
    path('', views.index),
    path('creat/', views.create),
    path('read/<id>/', views.read)
]
