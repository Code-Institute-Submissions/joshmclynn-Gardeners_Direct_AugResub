from django import forms
from .models import Products



class admin_product_form(forms.ModelForm):
    class Meta:
        model = Products
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)