from django.conf.urls import url, include
from django.urls import path 
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'event', EventModelViewSet, base_name='event')
router.register(r'event-time', EventTimeModelViewSet, base_name='event-time')
router.register(r'participant', ParticipantModelViewSet, base_name='participants')
router.register(r'club', ClubModelViewSet, base_name='club')
router.register(r'member', MemberModelViewSet, base_name='member')
router.register(r'attendance', AttendanceModelViewSet, base_name='attendance')

urlpatterns = router.urls
