from rest_framework import serializers
from .models import *


class EventModelDepthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
        read_only_fields = ('id','created_timestamp',)
        depth = 2


class EventModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
        read_only_fields = ('id', 'created_timestamp',)


class EventTimeModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EventTime
        fields = ('id', 'event', 'start_time', 'end_time')
        read_only_fields = ('created_timestamp', 'updated_timestamp')


class ClubHyperlinkedModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Club
        fields = ('id', 'name', 'description', 'icon',
                  'created_timestamp', 'updated_timestamp')
        read_only_fields = ('created_timestamp', 'updated_timestamp')


class MemberModelSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Member
        fields = ('id', 'user', 'club', 'status', 'position',
                  'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')


class ParticipantModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = '__all__'


class AttendanceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'
