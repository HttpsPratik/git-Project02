from django.urls import path
from .views import RegisterAPI, VerifyOtpAPI, LoginAPI

app_name = 'dashboard'

urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('verify/', VerifyOtpAPI.as_view(), name='verify'),
    path('login/', LoginAPI.as_view(), name='login'),
   
]





