from django.contrib import admin
from django.urls import path
from profiles import views


urlpatterns = [
    
    path('', views.profile, name = 'profile'),
    path('delete_profile/', views.delete_profile, name = 'delete_profile')
]