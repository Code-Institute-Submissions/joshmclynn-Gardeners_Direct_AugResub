from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
from .models import sub_user_details
from django.shortcuts import get_object_or_404
from profiles.models import UserProfile
from .forms import checkout_form
import math





@login_required
def quote(request):
    
    user_total = UserProfile.objects.get(user=request.user)
    
    total=user_total.quote

    return render(request, 'quote.html',{'total':total})
    
    
         
@login_required        
def checkout(request):
    
    profile = get_object_or_404(sub_user_details,user=request.user,subscription_cost=request.quote)
    
    if request.method=='POST':
        form = checkout_form(request.POST,profile=instance)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request,
                           ('update failed'))
    else:
        form = checkout_form(instance=profile)
    return render(request,'checkout.html',{'form':form})
    
    
