from django import forms

from .models import Newsletter


class newsletter_form(forms.ModelForm):
    
    class Meta:
        model = Newsletter
        fields = "__all__"
    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
    