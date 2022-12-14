from django.http import HttpResponse,HttpResponseRedirect
from django.template.loader import render_to_string
from django.conf import settings
from .models import sub_user_details
from profiles.models import UserProfile






class stripe_wh_handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        
            
        return HttpResponseRedirect(redirect_to='/')(
            content=(f'Webhook received: {event["type"]} | Fail: '
                         ''),
            status=200)
        

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)