from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
from .models import sub_user_details
from django.shortcuts import get_object_or_404
from profiles.models import UserProfile
from django.conf import settings
import math
import stripe






@login_required
def quote(request):
    
    user_total = UserProfile.objects.get(user=request.user)
    
    total=user_total.quote

    return render(request, 'quote.html',{'total':total})
    
    
         






@login_required
def checkout_user(request):
    
    
    if request.user.is_authenticated:
        user_details = sub_user_details.objects.get(user=request.user)
        user_address = UserProfile.objects.get(user=request.user)
        
        form_data = {
            'username': user_details.user,
            'quote': user_details.subscription_cost,
            'address':user_address.First_line_address
        
            }
        
        
    
        template = 'checkout.html'
        context = {
            'order_form':form_data,
            'stripe_public_key':'pk_test_51LNIUlAbUEDkhRpYcKIlXfwwetfZO0yrL7CogWC0NNu5wRXHohbtEg48YfOb8ceryEElipqo7lg1MuqD5vsT1T5I00VpXiJ3qR',
            'client_secret':'test client secret'
        }
    
        return render(request,template,context)
    else:
        return redirect(request, 'accounts/signup.html')
    
