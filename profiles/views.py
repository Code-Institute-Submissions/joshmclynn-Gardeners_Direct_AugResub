from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm


@login_required
def profile(request):
    
    profile = get_object_or_404(UserProfile,user=request.user)
    
    if request.method=='POST':
        form = UserProfileForm(request.POST,instance=profile)
        if form.is_valid():
            form.save()
            message.success(request,'Profile updated Successfully')##sweetify
        else:
            messages.error(request,
                           ('update failed'))
    else:
        form = UserProfileForm(instance=profile)
        
    template = 'profiles/profile.html'
    context = {
        'form':form,
    }
    
    return render(request,template,context)

# Create your views here.
