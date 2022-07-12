from django.shortcuts import render
from .forms import subscriptioncalculator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect



@login_required
def quote(request):
   
    if request.method == 'POST':
        form = subscriptioncalculator(request.POST)
        
        if form.is_valid():
            return HttpResponseRedirect('index.html')##quote())
        
    else:
        form = subscriptioncalculator()   

    return render(request,'quote.html', {'form':form})



##def quote():
    

   
# Create your views here.
