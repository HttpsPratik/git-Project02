
from django.db import models
from django.urls import reverse



class Comment(models.Model):
    
    email = models.EmailField(max_length=59)
    title = models.CharField(max_length=20)
    description = models.TextField()
    

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('DetailView', args=[str(self.id)])


