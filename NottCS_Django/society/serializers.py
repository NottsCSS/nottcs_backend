from rest_framework import serializers
from .models import *

class EventModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('event_title','event_desp','event_start','event_end','created_timestamp','organizing_chairman','status','image','fees','event_venue')
        read_only_fields = ('created_timestamp',)

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
            "user",
            "event_id",
            "attendance",
            "additional_info",
            "feedback"
        )