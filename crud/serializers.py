import email
from rest_framework import serializers
from crud.models import Comment

class CommentSerializer(serializers.HyperlinkedModelSerializer):
 
    class Meta:
        model = Comment
        fields = '__all__'


  #For Decoration      
# class UsersSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = users
#         fields = '__all__'