from dataclasses import field
from rest_framework import serializers
from accounts.models import CustomUser


class CustomUserSerializer(serializers.Serializer):
    email= serializers.EmailField(max_length=40)
    password = serializers.CharField()
    is_verified= serializers.BooleanField(default=False)

    def create(self, validated_data):
        return CustomUser.objects.create(**validated_data)


class VerifyAccountSerializer(serializers.Serializer):

    email = serializers.EmailField()
    otp = serializers.CharField()
    
    

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()