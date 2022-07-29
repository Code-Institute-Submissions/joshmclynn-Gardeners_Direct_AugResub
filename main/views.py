from django.shortcuts import render, redirect
from .forms import newsletter_form

# Create your views here.
def index(request):
    
    
    form = newsletter_form(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('')
    
    context ={
        'form':form
    }    
    return render(request, 'home/index.html', context)