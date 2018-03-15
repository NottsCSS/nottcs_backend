from rest_framework import serializers
from .models import *

class EventModelDepthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id','title','description','created_timestamp','organizing_club','organizing_chairman','status','image','fees','venue')
        read_only_fields = ('id','created_timestamp',)
        depth = 2

class EventModelCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id','title','description','created_timestamp','organizing_club','organizing_chairman','status','image','fees','venue')
        read_only_fields = ('id','created_timestamp',)

class EventTimeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventTime
        fields = ('id','event', 'start_time','start_time')
        read_only_fields = ('created_timestamp','updated_timestamp')


class ClubModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ('id','name', 'description','icon','created_timestamp','updated_timestamp')
        read_only_fields = ('created_timestamp','updated_timestamp')

class MemberSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Member
        fields = ('id', 'user', 'club', 'status', 'position', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')

class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = (
            'id',
            "user",
            "event",
            "additional_file",
            "additional_info",
            "feedback"
        )

class AttendanceSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = Attendance
        fields = ('id', 'participant', 'event_time', 'attendance')