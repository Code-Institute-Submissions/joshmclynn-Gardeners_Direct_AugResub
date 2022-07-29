from django.shortcuts import render,redirect,reverse,get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
from .models import sub_user_details
from profiles.models import UserProfile
from django.conf import settings
from admin_products.models import Products
from .forms import sub_address_form
import math
import stripe
import sweetify






@login_required
def quote(request):
    
    total = UserProfile.objects.get(user=request.user).quote
    product_details = Products.objects.all()
    print(total)
    context = {
        'product_details':product_details,
        'total':total
    }
    template = 'quote.html'
    return render(request, template, context)
    
    
         
@require_POST
def cache_checkout_data(request):
    
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, ('Sorry, your payment cannot be '
                                 'processed right now. Please try '
                                 'again later.'))
        return HttpResponse(content=e, status=400)





@login_required
def checkout_user(request):
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    stripe_public_key = settings.STRIPE_PUBLISHABLE_KEY
    user_details = UserProfile.objects.get(user=request.user)
    if request.method=='POST':
        form = sub_address_form()
        if form.is_valid():
            form.save()
        return redirect(reverse('checkout_success'))
              
            
            
            
    total = user_details.quote
    stripe_total = round(total *100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(   
    amount=stripe_total,
    currency=settings.STRIPE_CURRENCY,
    description={
        user_details.user,
        user_details.First_line_address
            }
    )
    form = sub_address_form()
    profile = get_object_or_404(UserProfile,user=request.user)
    print(profile)
    template = 'checkout.html'
    context = {
            'form':form,
            'stripe_public_key':stripe_public_key,
            'client_secret':intent.client_secret,
            }   
            
    return render(request,template,context)
        
    
    
    



def checkout_success(request):
    """
    Handle successful checkouts
    """
    

    if request.user.is_authenticated:
        
        user = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        object_sub = sub_user_details(user=request.user,subscription_cost=user.quote,paid=True)
        
        object_sub.save()

   

    template = 'checkout_success.html'
    context = {
        sub_user_details.objects.get(user=request.user)
    }

    return render(request, template,context)