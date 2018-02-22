from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from .serializers import *
from .models import *

class EventViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Event.objects.all()
    serializer_class = EventModelSerializer
    	
    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
		
        queryset = Event.objects.all()
        event_title = self.request.query_params.get('event_title', None)
        #organizing_club = self.request.query_params.get('organizing_club', None)
        if event_title is not None:
            queryset = queryset.filter(event_title=event_title)
        #if organizing_club is not None:
            #queryset = queryset.filter(organising_club=organizing_club)
        return queryset



class MemberCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new member."""
        serializer.save()

class MemberDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class show the details of the member like name, club, status and position."""

    queryset = Member.objects.all()
    serializer_class = MemberSerializer        
