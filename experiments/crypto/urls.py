from django.contrib import admin
from django.urls import path, include

from . import views
urlpatterns = [
    path('',    views.index, name='index'),
    path('rsa', views.rsa,   name='rsa'),
    path('rsa/', views.rsa,   name='rsa'),
    path('des', views.des,   name='des'),
    path('des/', views.des,   name='des'),
]
