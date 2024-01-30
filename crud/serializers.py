import email
from rest_framework import serializers
from crud.models import Comment


class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=59)
    title = serializers.CharField(max_length=20)
    description = serializers.CharField()

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance