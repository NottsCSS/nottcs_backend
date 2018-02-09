from rest_framework import serializers
from .models import AzureADUser


class AzureADUserSerializer(serializers.ModelSerializer):
    '''
    Model serializers for the azure ad user.
    '''
    class Meta:
        model = AzureADUser
        exclude = ('is_authenticated', 'date_joined', )
        read_only_fields = ('name', 'email',)
