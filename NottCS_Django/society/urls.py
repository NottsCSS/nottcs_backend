from django.conf.urls import url, include
from django.urls import path 
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'event', EventViewSet, base_name='event')
router.register(r'club', ClubViewSet, base_name='club')
urlpatterns = {
    url(r'^member/$', MemberCreateView.as_view(), name="create"),
    url(r'^member/(?P<pk>[0-9]+)/$',MemberDetailsView.as_view(), name="details"),
    
    #Create participant
    path('participantcreate/', ParticipantCreateView.as_view()),
    # Return a list of event that has been participated by the user
    # Format : /participantdetail?user=
    path('participantdetail/', ParticipantDetail.as_view()),
    # Return a list of event participants
    # Format : /event/?event_id=
    path('eventparticipant/', EventParticipantList.as_view()),
}

urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += router.urls
