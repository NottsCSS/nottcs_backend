from django.shortcuts import render
from rest_framework import generics,views, status
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import *
from .models import *
import json

class EventView(views.APIView):
    '''
    def get(self, request):
        event = Event.objects.all()
        serializer = EventModelDepthSerializer(data=event)
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    '''
    def post(self, request):
        data = request.data
        event_serializer = EventModelCreateSerializer(data=data)
        if event_serializer.is_valid(raise_exception=True): 
            event_serializer.save()
            data = data['time']
            for i in range(len(data)):
                data[i]['event'] = event_serializer.data['id']
            
            eventtime_serializer = EventTimeModelSerializer(data=data,many=True)
            if eventtime_serializer.is_valid(raise_exception=True): 
                eventtime_serializer.save()
                return Response(eventtime_serializer.data)
            return Response(eventtime_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(event_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ParticipantView(views.APIView):
    def post(self, request):
        data = request.data
        participant_serializer = ParticipantSerializer(data=data)
        if participant_serializer.is_valid(raise_exception=True): 
            participant_serializer.save()
            data = []

            event_time = EventTime.objects.filter(event__id=participant_serializer.data['event']).values('id')
            for i in range(len(event_time)):
                data.append({"participant":participant_serializer.data['id'],"event":event_time[i]})

            attendance_serializer = AttendanceSerializer(data=data,many=True)
            if attendance_serializer.is_valid(raise_exception=True): 
                attendance_serializer.save()
                return Response(attendance_serializer.data)
            return Response(attendance_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(participant_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EventViewSet(viewsets.ModelViewSet):

    queryset = Event.objects.all()
    #serializer_class = EventModelSerializer
    
    def get_serializer_class(self):
        if self.action == 'create':
            return EventModelCreateSerializer
        else:
            return EventModelDepthSerializer(1)

    def get_queryset(self):
		
        queryset = Event.objects.all()
        title = self.request.query_params.get('title', None)
        #organizing_club = self.request.query_params.get('organizing_club', None)
        if title is not None:
            queryset = queryset.filter(title=title)
        #if organizing_club is not None:
            #queryset = queryset.filter(organising_club=organizing_club)
        return queryset

class EventTimeViewSet(viewsets.ModelViewSet):

    queryset = EventTime.objects.all()
    serializer_class = EventTimeModelSerializer
        
    def get_queryset(self):
    
        queryset = EventTime.objects.all()
        return queryset


class ClubViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubModelSerializer
        
    def get_queryset(self):
        
        
        queryset = Club.objects.all()
        Club_name = self.request.query_params.get('club_name', None)
        #User_Pk = self.request.query_params.get('User_Pk', None)
        if Club_name is not None:
            queryset = queryset.filter(club_name__icontains=Club_name)
        #if User_Pk is not None:
        #    queryset.objects.filter( User_Pk__contains=User_Pk )
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

class ParticipantCreateView(generics.ListCreateAPIView):
    """Collect attendance, feedback and additional information in this view"""
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer

class ParticipantDetail(generics.ListAPIView):
    """Return a list of event that has been participated by the user"""
    serializer_class = ParticipantSerializer
    def get_queryset(self):
        
        queryset = Participant.objects.all()
        username = self.request.query_params.get('user', None)
        if username is not None:
            queryset = queryset.filter(user__icontains=username)
        return queryset

class EventParticipantList(generics.ListAPIView):
    """Return a list of event participants given the correct event_id"""
    serializer_class = ParticipantSerializer
    def get_queryset(self):
        
        queryset = Participant.objects.all()
        event_id = self.request.query_params.get('event_id', None)
        if event_id is not None:
            queryset = queryset.filter(event_id__icontains=event_id)
        return queryset    
