import imp
from django.contrib import admin
from django.urls import path
import account
from devapp import views
from account import views as account_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('postcreate/', views.postcreate, name='postcreate'),
    path('detail/<int:post_id>', views.detail, name='detail'),
    path('new_comment/<int:post_id>', views.new_comment, name='new_comment'),
    path('login/', account_views.login, name='login'),
    path('logout/', account_views.logout, name='logout'),
    path('freehome', views.freehome, name='freehome'),
    path('freepostcreate/', views.freepostcreate, name='freepostcreate'),
    path('freedetail/<int:post_id>', views.freedetail, name='freedetail'),
    path('new_freecomment/<int:post_id>', views.new_freecomment, name='new_freecomment'),
    path('sign_up/', account_views.sign_up, name='sign_up'),
]
