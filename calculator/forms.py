from django import forms
from .models import sub_user_details
from django.forms import ModelForm
from profiles.models import UserProfile
from .models import sub_user_details



class sub_address_form(forms.ModelForm):
    class Meta:
        model = sub_user_details
        exclude = {
            'user','subscription_cost','subscription_number','paid'
        }
    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)   