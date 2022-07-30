from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [

    path('', views.index, name='home'),
    path('email_add', views.email_add, name='email_add')
]
