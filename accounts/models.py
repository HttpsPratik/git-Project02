from django.contrib.auth.models import AbstractUser
from django.db import models

from .manager import UserManager


class CustomUser(AbstractUser):
    
    email = models.EmailField(unique=True)
    is_verified = models.BooleanField(default=False)
    otp_code = models.CharField(max_length=6, blank=True, null=True)
    username = models.CharField(max_length=150, unique=False, blank=True, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = UserManager()
    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.email
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email

    
   

    