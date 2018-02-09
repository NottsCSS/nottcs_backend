from django.test import TestCase
from .models import AzureADUser
from rest_framework import status
class AzureADUserModelTest(TestCase):
    '''
    Test on the AzureADUserModel
    Some simple test to make sure the design of the models
    work as intended
    '''
    def setUp(self):
        AzureADUser.objects.create(
            name = "user",
            email = "user@somemail.com",
        )
        AzureADUser.objects.create(
            name = "user2",
            email = "user2@somemail.com",
            student_id = 20012133,
            library_no = 2001331231,
        )
    
    def test_user_can_have_null_student_id(self):
        user = AzureADUser.objects.get(email="user@somemail.com")
        user2 = AzureADUser.objects.get(email="user2@somemail.com")
        self.assertEqual(user.student_id, None)
        self.assertEqual(user2.student_id, 20012133)
    
    def test_user_can_have_null_library_no(self):
        user = AzureADUser.objects.get(email="user@somemail.com")
        user2 = AzureADUser.objects.get(email="user2@somemail.com")
        self.assertEqual(user.library_no, None)
        self.assertEqual(user2.library_no, 2001331231)


class AzureADSocialAuthenticationTest(TestCase):
    '''
    Test on the Authentication for the AzureADUser

    '''
    def setUp(self):
        AzureADUser.objects.create(
            name = "user",
            email = "user@somemail.com",
            student_id = 20012133,
            library_no = 2001331231,
        )
    
    def test_failed_authentication_get(self):
        auth = 'Bearer faketoken1234'
        response = self.client.get(
            '/azuread-user/me/', HTTP_AUTHORIZATION=auth
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_failed_authentication_put(self):
        auth = 'Bearer faketoken1234'
        response = self.client.put(
            '/azuread-user/me/',
            data={'student_id':20012233,'library_no':200131234}, 
            HTTP_AUTHORIZATION=auth
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)