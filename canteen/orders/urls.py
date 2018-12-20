from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[
    path('',views.list_of_dishes,name='list_of_dishes'),
]