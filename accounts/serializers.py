from dataclasses import field
from rest_framework import serializers
from accounts.models import CustomUser


class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = [ 'email', 'password', 'is_verified']


class VerifyAccountSerializer(serializers.Serializer):

    email = serializers.EmailField()
    otp = serializers.CharField()
    

class LoginSerializer(serializers.HyperlinkedModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField()