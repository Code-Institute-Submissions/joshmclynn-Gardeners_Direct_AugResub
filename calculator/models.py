import uuid
from django.db import models
from django.db.models import Model
from django.db import models
from django.contrib.auth.models import User
from profiles.models import UserProfile
from django.dispatch import receiver
from django.conf import settings

from profiles.models import UserProfile
# Create your models here.




class sub_user_details(models.Model):
    
    
    subscription_number = models.CharField(max_length=32, null=False, editable= False)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    subscription_cost = models.FloatField(default=0)
    paid = models.BooleanField(default=False)
    
    
    def _generate_subscription_number(self, *args, **kwargs):
        
        return uuid.uuid4().hex.upper()
    
    
    def _generate_subscription_cost_(self):
        self.subscription_cost=UserProfile.quote(user=request.user)
    
    
    def save(self,*args,**kwargs):
        if not self.subscription_number:
            self.subscription_number=self._generate_subscription_number()
            super().save(*args, **kwargs)
        
        
    def __str__(self):
        return self.subscription_number
    
        
    
    
        
        
        
                
                
                
        