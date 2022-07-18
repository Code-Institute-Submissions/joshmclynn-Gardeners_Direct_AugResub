from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
from .models import sub_user_details
from django.shortcuts import get_object_or_404
from profiles.models import UserProfile
from .forms import checkout
import math





@login_required
def quote(request):
    
    total = UserProfile.objects.get(user=request.user)
    
    print(total.quote)
    
    return render(request, 'quote.html',)
    
    ##pph = 25
    #onehrarea = 14
    #iri = 5
    #grs = 5
    #profile = UserProfile.objects.get(user=request.user)
    #length = profile.garden_length
    #width = profile.garden_width
    #irrigation = profile.irrigation
    #grass = profile.grass
    #area = math.ceil((width*length)/onehrarea)
    
    #if (area<=1):
     #   total=pph
    #else:
    #    total=(area*pph)
        
    #if (irrigation==True):
    #    total=(total+iri)   
    #if (grass==True):
    #    total=(total+grs)
        
    
        
    
    #profile = get_object_or_404(sub_user_details,user=request.user,quote=total)
    #print(profile)
    
    #if request.method=='POST':
    #    form = checkout(request.POST,instance=profile)
    #if form.is_valid():
    #    form.save()
    #    messages.success(request, 'Profile updated successfully')"""
         
        
    

    
    



    