from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField()
    name = serializers.CharField()
    phone = serializers.CharField()
    password = serializers.CharField(write_only=True)
    google_token = serializers.JSONField(read_only=True)
    is_staff = serializers.BooleanField(read_only=True)

class HostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField()
    name = serializers.CharField()
    phone = serializers.CharField()


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

class RedirectSerializer(serializers.Serializer):
    code = serializers.CharField()

