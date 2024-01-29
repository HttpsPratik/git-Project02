from django.urls import path
from .views import RegisterAPI, VerifyOtpAPI, LoginAPI
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
app_name = 'dashboard'

urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('verify/', VerifyOtpAPI.as_view(), name='verify'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]





