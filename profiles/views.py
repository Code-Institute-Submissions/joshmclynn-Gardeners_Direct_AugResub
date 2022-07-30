from django.shortcuts import render, get_object_or_404,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile,User
from .forms import UserProfileForm
from calculator.models import sub_user_details
import sweetify



@login_required
def profile(request):
    
    profile = get_object_or_404(UserProfile,user=request.user)
    print(profile)
    if request.method=='POST':
        form = UserProfileForm(request.POST,instance=profile)
        if form.is_valid():
            form.save()
            sweetify.success(request, title='Profile updated successfully')
            return redirect('/')
        else:
            messages.error(request,
                           ('update failed'))
    else:
        form = UserProfileForm(instance=profile)
        
    if sub_user_details.objects.filter(user__username__contains=profile.user):
        subs = get_object_or_404(sub_user_details,user=request.user)
        load_sub = subs
        
        
        
    else:
        load_sub = 'Your Dont have a purchase yet'
    
        
    template = 'profiles/profile.html'
    context = {
        'form':form,
        'load_sub':load_sub
        
    }
    
    
    return render(request,template,context)

# Create your views here.
@login_required
def delete_profile(request):
    try:
        a = User.objects.get(username=request.user)
        a.delete()
        sweetify.success(request, title='Your profile has been deleted!')
    except User.DoesNotExist:
        sweetify.error(request, title='Profile does not exist')

    return redirect(to='index')