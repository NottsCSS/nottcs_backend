from django.shortcuts import render
from rest_framework import generics, views, status
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import *
from .models import *


class EventModelViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventModelSerializer

    def get_queryset(self):
        queryset = Event.objects.all()
        title = self.request.query_params.get('title', None)
        club = self.request.query_params.get('club', None)
        if title is not None:
            queryset = queryset.filter(title__icontains=title)
        if club is not None:
            queryset = queryset.filter(organizing_club__name__icontains=club)
        return queryset


class EventTimeModelViewSet(viewsets.ModelViewSet):
    serializer_class = EventTimeModelSerializer

    def get_queryset(self):
        queryset = EventTime.objects.all()
        event = self.request.query_params.get('event', None)
        if event is not None:
            queryset = queryset.filter(event__title__icontains=event)
        return queryset


class ClubModelViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubHyperlinkedModelSerializer

    def get_queryset(self):
        queryset = Club.objects.all()
        club_name = self.request.query_params.get('clubName', None)
        if club_name is not None:
            queryset = queryset.filter(name__icontains=club_name)
        return queryset


class MemberModelViewSet(viewsets.ModelViewSet):
    serializer_class = MemberModelSerializer

    def get_queryset(self):
        queryset = Member.objects.all()
        club = self.request.query_params.get('club', None)
        username = self.request.query_params.get('username', None)
        user_id = self.request.query_params.get('userID', None)
        if club is not None:
            queryset = queryset.filter(club__name__icontains=club)
        if username is not None:
            queryset = queryset.filter(user__name__icontains=username)
        if user_id is not None:
            queryset = queryset.filter(user__pk=user_id)
        return queryset


class ParticipantModelViewSet(viewsets.ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantModelSerializer

    def list(self, request):
        queryset = Participant.objects.all()
        user_id = request.query_params.get('userID', None)
        username = request.query_params.get('username', None)
        event_id = request.query_params.get('eventID', None)
        if user_id is not None:
            queryset = Participant.objects.filter(
                user__id=user_id)
        if username is not None:
            queryset = Participant.objects.filter(
                user__name__icontains=username)
        if event_id is not None:
            queryset = Participant.objects.filter(event__id=event_id)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class AttendanceModelViewSet(viewsets.ModelViewSet):
    serializer_class = AttendanceModelSerializer

    def get_queryset(self):
        queryset = Attendance.objects.all()
        event_id = self.request.query_params.get('eventID', None)
        participant_id = self.request.query_params.get('participantID', None)
        if event_id is not None:
            queryset = queryset.filter(event_time__event__id=event_id)
        if participant_id is not None:
            queryset = queryset.filter(participant__id=participant_id)
        return queryset
