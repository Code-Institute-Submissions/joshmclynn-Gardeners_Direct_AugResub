from django.shortcuts import render
from .forms import subscriptioncalculator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import sub_user_details
from django.contrib.auth import get_user_model



@login_required
def quote(request):
    if request.method == 'POST':
        form = subscriptioncalculator(request.POST)
        
        if form.is_valid():
            form.save(request)
            return render('quote_amount.html')##quote())
        
    else:
        form = subscriptioncalculator()   

    return render(request,'quote.html', {'form':form})




def quotation(request):
        context = {}
        context = sub_user_details.objects.values()
        print(context)
        total_area = (request.user.garden_length*request.user.garden_width)
        irrigation_price = 20
        grass_price = 5
        average_size = 14
        price = 25
        area_cost = 0
        tot=(total_area/average_size)
        if tot<=average_size:
            area_cost = 25
        else:
            area_cost = (tot*price)
        if irrigation == True:
            area_cost +=irrigation_price
        if grass ==True:
            area_cost +=grass_price
            
            
        data = area_cost    
            
        return render(request,'quote_amount.html', {'data':data})




##def quote():
    

   
# Create your views here.
