from email import message
from django.core.mail import send_mail
from dashboard.models import CustomUser
import random
from django.conf import settings


def send_otp (email):
    subject ="Email verification account"
    otp=random.randint(1000, 9999)
    message= f'Your otp code is {otp}'
    email_from=settings.EMAIL_HOST
    send_mail(subject,message,email_from,[email])
    CustomUser_object= CustomUser.objects.get(email=email)
    CustomUser_object.otp= otp
    CustomUser_object.save()