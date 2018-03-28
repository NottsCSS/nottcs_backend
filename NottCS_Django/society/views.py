from django.shortcuts import render
from rest_framework import generics, views, status
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import *
from .models import *


class EventModelViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'create':
            return EventModelSerializer
        else:
            return EventModelDepthSerializer

    def get_queryset(self):
        queryset = Event.objects.all()
        title = self.request.query_params.get('title', None)
        #organizing_club = self.request.query_params.get('organizing_club', None)
        if title is not None:
            queryset = queryset.filter(title=title)
        # if organizing_club is not None:
            #queryset = queryset.filter(organising_club=organizing_club)
        return queryset


class EventTimeModelViewSet(viewsets.ModelViewSet):
    queryset = EventTime.objects.all()
    serializer_class = EventTimeModelSerializer


class ClubModelViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubHyperlinkedModelSerializer

    def get_queryset(self):
        queryset = Club.objects.all()
        club_name = self.request.query_params.get('club_name', None)
        # user_pk = self.request.query_params.get('user_pk', None)
        if club_name is not None:
            queryset = queryset.filter(club_name__icontains=club_name)
        # if User_Pk is not None:
        #    queryset.objects.filter( User_Pk__contains=User_Pk )
        return queryset


class MemberModelViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberModelSerializer


class ParticipantModelViewSet(viewsets.ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantModelSerializer

    def list(self, request):
        queryset = Participant.objects.all()
        username = request.query_params.get('username', None)
        event_id = request.query_params.get('event_id', None)
        if username is not None:
            queryset = Participant.objects.filter(
                user__name__icontains=username)
        if event_id is not None:
            queryset = Participant.objects.filter(event___icontains=event_id)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class AttendanceModelViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceModelSerializer
