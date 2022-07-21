from django.contrib import admin
from .models import sub_user_details

# Register your models here.


class sub_user_detailsAdmin(admin.ModelAdmin):
    
    readonly_fields = ('subscription_cost',
                       'subscription_number',
                       'user')
    
    

admin.site.register(sub_user_details,sub_user_detailsAdmin)
    