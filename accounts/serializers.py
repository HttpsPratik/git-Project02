from dataclasses import field
from rest_framework import serializers
from accounts.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [ 'email', 'password', 'is_verified']

    # def create(self, validated_data):
    #     return CustomUser.objects.create(**validated_data)


class VerifyAccountSerializer(serializers.Serializer):

    email = serializers.EmailField()
    otp = serializers.CharField()
    
    

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()