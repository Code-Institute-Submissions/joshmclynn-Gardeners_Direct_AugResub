from django.db import models
from django.db.models import Model
from django.contrib.auth.models import User
from profiles.models import UserProfile
from django.dispatch import receiver

# Create your models here.

class sub_user_details(models.Model):
    
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    quote = models.FloatField(default=0)
    
    
    
        
    
    
        
        
        
                
                
                
        