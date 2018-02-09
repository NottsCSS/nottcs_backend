from django.shortcuts import get_object_or_404
from rest_framework import views, status
from rest_framework.response import Response

from .serializers import AzureADUserSerializer
from .models import AzureADUser

class AzureADUserPersonalView(views.APIView):
    '''
    View to get the authenticated user details
    by refering to the authorization token passed.

    * Requires Azure AD authentication
    '''

    def get(self, request):
        '''
        Return personal user details
        '''
        user = get_object_or_404(AzureADUser, email=request.user.email)
        serializer = AzureADUserSerializer(user)
        return Response(serializer.data)

    def put(self, request):
        '''
        Update personal user details

        * Only allows edit for student_id and library_no.
        '''
        # Check validity of input
        serializer = AzureADUserSerializer(data=request.data)
        if serializer.is_valid():
            user = get_object_or_404(AzureADUser, email=request.user.email) # Finds and update the user
            user.student_id = serializer.data['student_id']
            user.library_no = serializer.data['library_no']
            user.save() # Save the changes

            # Return the updated user object
            return Response(AzureADUserSerializer(user).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
