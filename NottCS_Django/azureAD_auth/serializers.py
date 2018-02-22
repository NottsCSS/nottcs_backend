from rest_framework import serializers
from .models import AzureADUser


class AzureADUserSerializer(serializers.ModelSerializer):
    '''
    Model serializers for the azure ad user.
    '''
    def validate_student_id(self, value):
        '''
        Check if student_id is valid (must be int)
        '''
        try:
            int(value)
            return value
        except ValueError:
            raise serializers.ValidationError("Invalid Student ID.")

    def validate_library_no(self, value):
        '''
        Check if library_no is valid (must be int)
        '''
        try:
            int(value)
            return value
        except ValueError:
            raise serializers.ValidationError("Invalid Library Number.")

    class Meta:
        model = AzureADUser
        exclude = ('is_authenticated', 'date_joined', )
        read_only_fields = ('name', 'email',)
        # extra_kwargs = {'student_id': {'required': True}, 'library_no': {'required': True}}
        # Removed to allow ease of updating for front end
