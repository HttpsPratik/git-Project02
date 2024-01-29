from django.contrib.auth.models import AbstractUser
from django.db import models
# from datetime import datetime
# import secrets
from .manager import UserManager
# from django.contrib.auth import get_user_model
# from django.utils.crypto import get_random_string

class CustomUser(AbstractUser):
    
    email = models.EmailField(unique=True)
    # USERNAME_FIELD = email
    is_verified = models.BooleanField(default=False)
    otp_code = models.CharField(max_length=6, blank=True, null=True)
    # otp_expires_at = models.DateField(auto_now=True)
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

    
    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.email
        # if not self.pk:  
        #     self.otp_code = get_random_string(length=6)  
        super().save(*args, **kwargs)
# class OtpToken(models.Model):
#      user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="otps")
#      otp_code = models.CharField(blank=True, null=True)
#      otp_created_at = models.DateTimeField(auto_now_add=True)
#      otp_expires_at = models.DateTimeField(blank=True, null=True)
    
#      def __str__(self):
#          return self.user.username

    