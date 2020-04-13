from django.urls import path

from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('add', views.add, name='add'),
    path('delete', views.delete, name='delete'),
    path('list', views.list_files, name = 'list')
]
