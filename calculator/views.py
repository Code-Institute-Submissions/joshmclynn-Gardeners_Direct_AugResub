from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
from .models import sub_user_details
from django.shortcuts import get_object_or_404
from profiles.models import UserProfile
from django.conf import settings
import math
import stripe
import sweetify






@login_required
def quote(request):
    
    user_total = UserProfile.objects.get(user=request.user)
    
    total=user_total.quote

    return render(request, 'quote.html',{'total':total})
    
    
         
@require_POST
def cache_checkout_data(request):
    user_details = sub_user_details.objects.get(user=request.user)
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'quote': user_details.subscription_cost,
            'sub_num': user_details.subscription_number,
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
    user_details = sub_user_details.objects.get(user=request.user)
    
    if (user_details.subscription_cost ==0):
        sweetify.warning(request, """Your subscription doesnt exist!, try entering
                         details in the profile section!""")
    
    else:
        if request.user.is_authenticated:
            user_details = sub_user_details.objects.get(user=request.user)
            user_address = UserProfile.objects.get(user=request.user)
        
            form_data = {
                'username': user_details.user,
                'quote': user_details.subscription_cost,
                'address':user_address.First_line_address
        
                }
        
            total = user_details.subscription_cost
            stripe_total = round(total *100)
            stripe.api_key = stripe_secret_key
            intent = stripe.PaymentIntent.create(
                
                amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
            description={
                user_details.user,
                user_details.subscription_number
            }
            )
            
    
            template = 'checkout.html'
            context = {
                'order_form':form_data,
                'stripe_public_key':stripe_public_key,
                'client_secret':intent.client_secret,
            }
    
            return render(request,template,context)
        else:
            return redirect(request, 'accounts/signup.html')
    
