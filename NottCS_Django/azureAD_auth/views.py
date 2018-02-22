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

    def patch(self, request):
        '''
        Update personal user details

        * Only allows edit for fields not related to username and email
        '''
        # Check validity of input
        serializer = AzureADUserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = get_object_or_404(AzureADUser, email=request.user.email) # Finds and update the user
            # Do checks for each data, if they exists, update, else dont update.
            if serializer.data.get('student_id'):
                user.student_id = serializer.data.get('student_id')
            if serializer.data.get('library_no'):
                user.library_no = serializer.data.get('library_no')
            if serializer.data.get('year_of_study'):
                user.year_of_study = serializer.data.get('year_of_study')
            if serializer.data.get('course'):    
                user.course = serializer.data.get('course')
            user.save() # Save the changes

            # Return the updated user object
            return Response(AzureADUserSerializer(user).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
