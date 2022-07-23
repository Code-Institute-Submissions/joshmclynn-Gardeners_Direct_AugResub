from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.



class UserProfile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phoneNumber = models.CharField(max_length=20, null=True,blank=True)
    First_line_address = models.CharField(max_length=80,null=True,blank=True)
    Post_code = models.CharField(max_length=20,null=True,blank=True)
    garden_width = models.FloatField(default=0,blank=True)
    garden_length = models.FloatField(default=0,blank=True)
    irrigation = models.BooleanField(default=False)
    grass = models.BooleanField(default=False)
    quote = models.FloatField(default=0,editable=True,blank=True)
    
    
    
        
    def save(self, *args, **kwargs):
       
        area = (self.garden_length * self.garden_width)
        if area > 14:
            pp2 = (area/14)
            price = (pp2*25)
            self.quote = round(price,2)
        else:
            self.quote = 25
           
        super().save(*args, **kwargs)


    
    
    
    
    
    
    
    
    
    def __str__(self):
        return self.user.username
    
        
        
    
    
    
    

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    
    instance.userprofile.save()