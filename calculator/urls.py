from django.contrib import admin
from django.urls import path
from .import views



urlpatterns = [
    
    path('', views.quote, name = 'quote'),
    path('checkout/',views.checkout_user, name = 'checkout')
   
    
]