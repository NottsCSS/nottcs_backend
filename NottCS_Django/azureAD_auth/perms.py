from rest_framework import permissions
import requests  # Main library for making requests to microsoft graph api

from .models import AzureADUser


class IsAzureADAuthenticated(permissions.BasePermission):
    '''
    Custom Permission class tailored to the azure ad authentication
    PS: If there exists any better implementations this will be updated
    PS: This is currently replaced by the default built-in drf IsAuthenticated permission class
    '''

    def has_permission(self, request, view):
        '''
        This implementation should be used in any situation
        in which security bugs or implementation clashes happens
        '''

        graph_endpoint = 'https://graph.microsoft.com/v1.0/me/'
        headers = {'Authorization': request.auth}
        r = requests.get(url=graph_endpoint, headers=headers)
        response_json = r.json()

        # Check if the user actually exists and is authenticated
        if r.status_code != 200:
            return False
        return AzureADUser.objects.filter(
            email=response_json['mail'],
            name=response_json['displayName']
        ).exists()
