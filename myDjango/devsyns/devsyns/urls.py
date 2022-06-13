import imp
from django.contrib import admin
from django.urls import path
from devapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('postcreate/', views.postcreate, name='postcreate')
]
