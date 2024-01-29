from crud.models import Comment
from rest_framework import viewsets
from crud.serializers import CommentSerializer




class CommentViewsets(viewsets.ModelViewSet):
   queryset = Comment.objects.all()
   serializer_class = CommentSerializer
 