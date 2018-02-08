from django.contrib import admin
from .models import AzureADUser


# A simple register should be sufficient 
# for the azure ad user model
admin.site.register(AzureADUser)