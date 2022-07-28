from django.contrib import admin
from django.urls import path
from .import views
from .webhooks import webhook



urlpatterns = [
    
    path('', views.quote, name = 'quote'),
    path('checkout/',views.checkout_user, name = 'checkout'),
    path('checkout_success/',views.checkout_success, name = 'checkout_success'),
    path('cache_checkout_data/',
         views.cache_checkout_data,
         name='cache_checkout_data'),
    path('wh/',webhook, name='webhook')
   
    
]