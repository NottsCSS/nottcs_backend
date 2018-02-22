from django.urls import path

from .views import AzureADUserPersonalView

urlpatterns = [
    path('me/', AzureADUserPersonalView.as_view(), name='user_personal_view'),
]