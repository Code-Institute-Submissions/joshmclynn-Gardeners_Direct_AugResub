from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
from profiles.models import UserProfile
import math


@login_required
def quote(request):
    pph = 25
    onehrarea = 14
    iri = 5
    grs = 5
    profile = UserProfile.objects.get(user=request.user)
    length = profile.garden_length
    width = profile.garden_width
    irrigation = profile.irrigation
    grass = profile.grass
    area = math.ceil((width*length)/onehrarea)
    print(area)
    if (area<=1):
        total=pph
    else:
        total=(area*pph)
        print(total)
    if (irrigation==True):
        total=(total+iri)
    if (grass==True):
        total=(total+grs)
        
    
     
    ##print(UserProfile())
    ##print(request.user.garden_length)
   ## length ={}
    
   ## print(user)
    return total,render(request,'quote.html',{'total':total})