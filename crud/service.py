from crud.models import Comment

class CommentService:
    def get_all_comments(self):
        return Comment.objects.all()
    
    def get_comment_by_id(self,comment_id):
        try:
                Comment.objects.get(pk=comment_id)
        except Comment.DoesNotExist:
              return None    
                
    def create_comment(self,data):
            return Comment.objects.create(**data)
    
    def update_comment(self,data, comment,instance,validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        comment.save()
        return comment
    
    def delete_comment(self,comment):
            comment.delete()