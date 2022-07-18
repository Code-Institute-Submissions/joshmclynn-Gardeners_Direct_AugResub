from django import forms
from .models import sub_user_details
from django.forms import ModelForm
from profiles.models import UserProfile



class checkout(forms.ModelForm):
   
    class Meta:
        model = sub_user_details
        exclude = ('user','quote')

    def __init__(self, *args, **kwargs):
        """
 ##       Add placeholders and classes, remove auto-generated
 ##       labels and set autofocus on first field
##        """
        super().__init__(*args, **kwargs)
        