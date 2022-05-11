from django import views
from django.urls import path
from polls import views

urlpatterns = [
    path('', views.index),
    path('create/', views.create),
    # path('create/save', views.save),
    path('read/<id>/', views.read),
    path('delete/', views.delete),
    path('update/<id>/', views.update)
]
