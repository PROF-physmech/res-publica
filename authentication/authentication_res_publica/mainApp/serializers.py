from rest_framework import serializers
from .models import Users


class LoginSerializer(serializers.Serializer):
    login = serializers.CharField()
    password = serializers.CharField()

class ErrorSerializer(serializers.Serializer):
    message = serializers.CharField()

