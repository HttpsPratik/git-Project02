from django.urls import path
from .views import RegisterAPI, VerifyOtpAPI, LoginAPI

app_name = 'dashboard'

urlpatterns = [
    path('register', RegisterAPI.as_view(), name='register'),
    path('verify', VerifyOtpAPI.as_view(), name='verify'),
    path('login', LoginAPI.as_view(), name='login'),
]




# router = routers.DefaultRouter()
# router.register(r'register/', CustomUserSerializer,basename='CustomUser')
# router.register(r'verify/', VerifyAccountSerializer,basename='VerifyAccount')
# router.register(r'login/', LoginSerializer,basename='Login')
# # router.register(r'verify', VerifyViewsets)


    #  path('',include(router.urls)),
    # path('dashboard/home/', views.home, name="home"),
    

    #------For Email OTP------------#
    # path('signup/', views.signup),
    # path("", views.index.as_view(), name="index"),
    # path("register", views.signup.as_view(), name="register"),
    # path("verify-email/<slug:username>", views.verify_email.as_view(), name="verify-email"),
    # path("resend-otp", views.resend_otp.as_view(), name="resend-otp"),
    # path("login/", views.signin.as_view(), name="signin"),
    # path('login/', views.login,name="login"),
    # # path('code/', views.code,name="code"),
    # path('logout/', views.logout,name="logout"),
    
  
    
