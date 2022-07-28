
from django.db import models
from django.db.models import Model
from django.contrib.auth.models import User

# Create your models here.

class Products(models.Model):
    
    product = models.CharField(max_length=50,blank=True,null=False,unique=True)
    descriptions = models.CharField(max_length=250,blank=True,null=False)
    price = models.IntegerField()
    sale = models.BooleanField()

    
    def __str__(self):
        return self.product
    
    
        
    