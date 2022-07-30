from django.db import models
from django.db.models import Model

# Create your models here.
class Newsletter(models.Model):
    
    email = models.EmailField(max_length=50,unique=True)
    
    def __str__(self):
        return self.email