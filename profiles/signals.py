from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from .models import UserProfile
from calculator.models import sub_user_details

##@receiver(post_save,sender=UserProfile)
##def add_quote_to_sub_user(sender,instance,created,**kwargs):
   
##    profile=instance
##    if not created:
##        sub_user_details.objects.update_or_create(
##                                    subscription_cost=profile.quote,user=profile.user)
        
    
    
## creates, updates and deletes when UserProfile model is save()



