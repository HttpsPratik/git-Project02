from tokenize import Comment
from django.http import Http404
from crud.serializers import CommentSerializer
from crud.service import CommentService
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

class CrudListView(APIView):
    def get(self, request):
        comments = CommentService.get_all_comments()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            CommentService.create_comment(serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CrudDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self,pk):
        comment = CommentService.get_comment_by_id(pk)
        if comment is None:
            raise Http404("Doesn't exist")
        return comment
    
    def get(self, request):
        comment = self.get_object.all()
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def put(self, request, pk):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            CommentService.update_comment(serializer.validated_data)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        comment = self.get_object(pk)
        CommentService.delete_comment(comment)
        return Response({'success': True, 'message': 'User deleted successfully'})