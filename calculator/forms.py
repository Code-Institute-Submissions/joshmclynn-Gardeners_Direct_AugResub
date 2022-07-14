from django import forms
from .models import sub_user_details
from django.forms import ModelForm



class subscriptioncalculator(ModelForm):
    ##garden_width = forms.IntegerField(max_value=100,
    ##                                  label="""What is the width of your
    ##                                  garden in meters?""",
    ##                                  required=True)
    ##garden_length = forms.IntegerField(max_value=100,
     ##                                  label="""What is the length of your
     ##                                  garden in meters?""",
     ##                                  required=True)
    ##irrigation = forms.BooleanField(label="""Do you have irrigation in your
    ##                                garden?""",
    ##                                )
    ##grass = forms.BooleanField(label="""Does your garden have grass?""",
    ##                           )
    ##first_line = forms.CharField(max_length=50,
     ##                            label="""Please enter the first line of your
    ##                             address""",
    ##                             required=True)
    ##post_code = forms.CharField(max_length=6,
    ##                            label="""Please enter your post-code""",
    ##                            required=True)
    
    class Meta:
        model = sub_user_details
        fields = ['garden_length','garden_width','irrigation','grass','first_line','post_code']
        
    def save(self,request):
        sub_user_details = super(subscriptioncalculator, self).save(request)
        sub_user_details.user = self.request.user.username
        sub_user_details.garden_width = self.cleaned_data['garden_width']
        sub_user_details.garden_length = self.cleaned_data['garden_length']
        sub_user_details.irrigation = self.cleaned_data['irrigation']
        sub_user_details.grass = self.cleaned_data['grass']
        sub_user_details.first_line = self.cleaned_data['first_line']
        sub_user_details.post_code = self.cleaned_data['post_code']
        sub_user_details.save()
        return sub_user_details

