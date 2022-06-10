import imp
from django.conf import settings
from django.contrib import admin
from django.urls import path
from blogapp import views
from account import views as account_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('formcreate/', views.formcreate, name='formcreate'),
    path('modelformcreate/', views.modelformcreate, name='modelformcreate'),
    path('detail/<int:blog_id>', views.detail, name="detail"),
    path('create_comment/<int:blog_id>', views.create_comment, name='create_comment'),
    path('login/', account_views.login,name='login' ),
    path('logout/', account_views.logout,name='logout' ),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)