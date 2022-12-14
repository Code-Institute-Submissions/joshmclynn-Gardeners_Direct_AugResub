from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [

    path('', views.site_owner, name='site_owner'),
    path('delete/<str:id>/', views.delete, name='delete'),
    path('delete_sub/<str:id>/', views.delete_sub, name='delete_sub'),
]
