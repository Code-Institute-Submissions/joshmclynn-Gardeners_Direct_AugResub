from django.shortcuts import render, get_object_or_404,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile,User
from .forms import UserProfileForm
import sweetify



@login_required
def profile(request):
    
    profile = get_object_or_404(UserProfile,user=request.user)
    
    if request.method=='POST':
        form = UserProfileForm(request.POST,instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('/')
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
@login_required
def delete_profile(request):
    try:
        a = User.objects.get(username=request.user)
        a.delete()
        sweetify.success(request, title='Your profile has been deleted!')
    except User.DoesNotExist:
        sweetify.error(request, title='Profile does not exist')

    return redirect(to='index')