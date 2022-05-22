from django.contrib import admin
from django.urls import path

import myapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myapp.views.home),
    path('test/', myapp.views.test),
]

SECRET_KEY = 'django-insecure-j)3!^-^pxmykei@tnx*@*bjr%+f)b1t+oyi*mdo1)z*(m$$@71'