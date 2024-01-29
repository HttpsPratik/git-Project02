
from django.db import models




class Comment(models.Model):
    
    email = models.EmailField(max_length=59)
    title = models.CharField(max_length=20)
    description = models.TextField()
    

    def __str__(self):
        return self.title
    


#For decoration
# class users(models.Model):
#     name = models.CharField(max_length=20)
#     age=models.IntegerField()
#     title = models.CharField(max_length=20)
#     description = models.TextField()