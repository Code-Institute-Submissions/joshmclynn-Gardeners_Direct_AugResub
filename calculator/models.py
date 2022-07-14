from django.db import models
from django.db.models import Model
from django.contrib.auth.models import User

# Create your models here.

class sub_user_details(models.Model):
    
                                     
    garden_width = models.FloatField()
    garden_length = models.FloatField()
    irrigation = models.BooleanField()
    grass = models.BooleanField()
    first_line = models.CharField(max_length=75)
    post_code = models.CharField(max_length=75)
    quote = models.FloatField(default=0)
    
        
        
                
                
                
        