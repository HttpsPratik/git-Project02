import email
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from accounts.models import CustomUser
from accounts.serializers import CustomUserSerializer, VerifyAccountSerializer, LoginSerializer
from accounts.email import send_otp
from django.utils import timezone
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterAPI(APIView):
    def post(self, request):
        try:
           
            data = request.data
            
            if 'email' not in data or not data['email']:
                return Response({
                    'status': 400,
                    'message': 'Email is required.',
    })
            user=CustomUser.objects.filter(email=data['email']).first()

            if user:
                return Response({
                'status': 400,
                'message': 'User already exist.',
            })

            serializer = CustomUserSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                send_otp(serializer.data['email'])
                
                
                return Response(data={
                    'status': 200,
                    'message': 'Registration successful. Check your email for verification.',
                    'data': serializer.data,
                })
           
            return Response({
                'status': 400,
                'message': 'Something went wrong',
                'data': serializer.errors,
            })

        except Exception as e:
            return Response({
                'status': 400,
                'message': 'Something went wrong',
                'data': {str(e)}
            })
            


    def get(self, request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response({
            'status': 200,
            'message': 'User list retrieved successfully',
            'data': serializer.data,
        })


class VerifyOtpAPI(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = VerifyAccountSerializer(data=data)
            if serializer.is_valid():
                email = serializer.validated_data['email']
                otp_code = serializer.validated_data['otp']
                try:
                    print(f"Attempting to verify email: {email}, OTP: {otp_code}")
                    user = CustomUser.objects.get(email=email, otp_code=otp_code)
                    if not user.is_verified:
                        user.is_verified = True
                        user.save()
                        return Response({
                            'status': 200,
                            'message': 'Account Verified',
                            'data': None,
                        })
                    else:
                        return Response({
                            'status': 200,
                            'message': 'User is already verified',
                            'data': serializer.data
                        })
                except CustomUser.DoesNotExist:
                    print(f"No user found with email: {email} and OTP: {otp_code}")
                    return Response({
                        'status': 400,
                        'message': 'Invalid email or OTP',
                        'data': None
                    })
            return Response({
                'status': 400,
                'message': 'Invalid input data',
                'data': serializer.errors
            })
        except Exception as e:
            print(f"Exception: {e}")
            return Response({
                'status': 500,
                'message': f'Internal Server Error: {str(e)}',
                'data': None
            })
    
class LoginAPI(APIView):
    def post(self, request):
        try:
            data = request.data
            user=CustomUser.objects.filter(email=data['email']).first()
            if user:
                return Response({
                'status': 400,
                'message': 'successfully logged in',
            })
            serializer = LoginSerializer(data=data)
            if serializer.is_valid():
                email = serializer.data['email']
                password = serializer.data['password']
                user = authenticate(request, email=email, password=password)
                if user is None:
                    return Response({
                        'status': 400,
                        'message': 'Invalid credentials',
                        'data': {},
                    })
                if not user.is_verified:
                    return Response({
                        'status': 400,
                        'message': 'Account is not verified',
                        'data': {},
                    })
                refresh = RefreshToken.for_user(user)

                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                })
            return Response({
                    'status': 400,
                    'message': 'Something went wrong',
                    'data': serializer.errors,
                })
        except Exception as e:
            print(e)

    def get(self, request):
        return Response({
            'status': 200,
            'message': 'GET request handled',
            'data': {},
        })