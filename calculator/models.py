from django.db import models
from django.db.models import Model

# Create your models here.

class sub_user_details(models.Model):
    ##user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     ##null=True, blank=True,)
    garden_width = models.FloatField()
    garden_length = models.FloatField()
    irrigation = models.BooleanField()
    grass = models.BooleanField()
    first_line = models.CharField(max_length=75)
    post_code = models.CharField(max_length=75)