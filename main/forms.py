from django import forms

from .models import newsletter


class newsletter_form(forms.ModelForm):
    
    class Meta:
        model = newsletter
        fields = "__all__"