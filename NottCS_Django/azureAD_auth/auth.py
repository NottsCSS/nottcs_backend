from django.contrib.auth.models import AnonymousUser
from rest_framework import authentication
from rest_framework import exceptions
import requests  # Main library for making requests to microsoft graph api

from .models import AzureADUser


class AzureADSocialAuthentication(authentication.BaseAuthentication):
    '''
    Custom authentication class for azure ad
    PS: If there exists any better implementations this will be updated
    '''
    keyword = 'bearer'  # Authorization header has the format 'Bearer <Token>'

    def authenticate(self, request):
        auth_token = authentication.get_authorization_header(request)
        auth_token_list = auth_token.split()

        # Check if the keyword is in the authorization header provided
        if not auth_token_list or auth_token_list[0].lower() != self.keyword.encode():
            return None
        
        # Check if a token is provided before proceeding
        if len(auth_token_list) == 1:
            msg = 'Invalid token header. No credentials provided.'
            raise exceptions.AuthenticationFailed(detail=msg)
        elif len(auth_token_list) > 2:
            msg = 'Invalid token header. Token string should not contain spaces.'
            raise exceptions.AuthenticationFailed(detail=msg)
        # Checking with the Azure AD backend
        # If token valid then get user details
        # If user not exist then create new user
        graph_endpoint = 'https://graph.microsoft.com/v1.0/me/'
        headers = {'Authorization': auth_token}
        r = requests.get(url=graph_endpoint, headers=headers)
        response_json = r.json()

        # Check status to determine if user exists
        if r.status_code == 200:
            # Check if email is nottingham.edu.my
            if response_json['mail'].split('@')[-1] != 'nottingham.edu.my':
                msg = 'You do not have permission to access this domain.'
                raise exceptions.PermissionDenied(detail=msg)

            # If the user can be queried from microsoft graph
            # And has the correct domain, then update or create
            user, created = AzureADUser.objects.update_or_create(
                email=response_json['mail'],
                defaults={
                    'name': response_json['displayName']
                }
            )
        else:
            # Pass back the error message from microsoft graph if error happens
            msg = response_json['error']['message']
            raise exceptions.AuthenticationFailed(detail=msg)

        # Returning a custom users for this third party authentication(Oauth2)
        # Will be updated if any other better implementation exists
        return (user, auth_token)
