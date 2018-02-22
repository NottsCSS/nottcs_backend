from django.contrib import admin
from .models import AzureADUser

@admin.register(AzureADUser)
class AzureADUserAdmin(admin.ModelAdmin):
    readonly_fields = ('is_authenticated','date_joined', )