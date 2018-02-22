from django.db import models

'''
Azure AD User Model
Does not contain password and act as a reference 
and a location to store student_id and library_no
'''
class AzureADUser(models.Model):
    name = models.CharField(max_length = 100, null=False)
    email = models.EmailField(unique=True, null=False)
    student_id = models.CharField(max_length = 20, blank=True, null=True)
    library_no = models.CharField(max_length = 30, blank=True, null=True)
    year_of_study = models.CharField(max_length = 30, null=False, default="1")
    course = models.CharField(max_length=50, blank=True)
    is_authenticated = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.email
