from rest_framework import serializers
from users.serializers import HostSerializer

class MeetingSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    summary = serializers.CharField()
    description = serializers.CharField()
    visitor_emails = serializers.ListSerializer(child=serializers.EmailField(), write_only=True)
    start_date = serializers.DateTimeField()
    end_date = serializers.DateTimeField()
    purpose = serializers.CharField()
    venue = serializers.CharField()

class InvitationSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    host = HostSerializer()
    meeting = MeetingSerializer(read_only=True)
    visitor_name = serializers.CharField(read_only=True)
    visitor_nric = serializers.CharField(read_only=True)
    visitor_email = serializers.EmailField(read_only=True)
    visitor_phone = serializers.CharField(read_only=True)
    is_preregistered = serializers.BooleanField(read_only=True)
    in_time = serializers.TimeField(read_only=True)
    out_time = serializers.TimeField(read_only=True)

class CheckInSerializer(serializers.Serializer):
    name = serializers.CharField()
    nric = serializers.CharField()


