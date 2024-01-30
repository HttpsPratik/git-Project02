from crud.models import Comment

class CommentService:
    def get_all_comments():
        return Comment.objects.all()
    
    def create_comment(data):
        return Comment.objects.create(**data)
    
    def update_comment(data, comment):
        comment.save()
        return comment
    
    def delete_comment(comment):
        comment.delete()