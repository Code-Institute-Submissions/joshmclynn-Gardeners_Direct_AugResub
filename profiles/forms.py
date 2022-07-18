from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user','quote')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        fields = {
            'phone_number': 'Phone Number',
            'postcode': 'Postal Code',
            'default_street_address1': 'Street Address 1',
            'garden_width':'What is the width of your garden in meters',
            'garden_length':'What is the length of your garden in meters',
            'irrigation':'Does your garden have irrigation',
            'grass':'Does your garden have grass',
        }