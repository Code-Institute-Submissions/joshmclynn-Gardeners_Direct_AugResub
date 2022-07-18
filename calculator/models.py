from django.db import models
from django.db.models import Model
from django.contrib.auth.models import User
from profiles.models import UserProfile
from .views import quote

# Create your models here.

class sub_user_details(models.Model):
    
    user_profile = models.OneToOneField(UserProfile,on_delete=models.CASCADE)
    quote = models.FloatField(quote.total)
    
        
        
                
                
                
        