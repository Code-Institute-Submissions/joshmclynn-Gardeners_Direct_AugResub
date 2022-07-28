from django.shortcuts import render, redirect
from .models import Products
from .forms import admin_product_form
from main import views
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView

import sweetify




def site_owner(request):
    
    
    # create object of form
    form = admin_product_form(request.POST or None, request.FILES or None)
     
    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()
        sweetify.success(request, title='Product added')
    else: 
        sweetify.error(request, title='Product already exists')
    
    product_details = Products.objects.all()
    context={'form':form,
             'product_details':product_details,}
    template = 'product_add.html'
    return render(request,template , context)




    
    

            

# Create your views here.



