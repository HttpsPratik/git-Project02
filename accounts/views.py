import email
import traceback
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from accounts.models import CustomUser
from accounts.serializers import CustomUserSerializer, VerifyAccountSerializer, LoginSerializer
from accounts.email import send_otp
from django.utils import timezone

class RegisterAPI(APIView):
    def post(self, request):
        try:
           
            data = request.data
            
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

            # return Response({
            #     'status': 500,
            #     'message': 'Internal Server Error',
            #     'data': None,
            # })
    # def post(self, request):
    #     try:
    #         data = request.data
    #         user=CustomUser.objects.filter(email=data['email']).first()
    #         if user:
    #                 return Response({
    #                     'status': 400,
    #                     'message': 'verified',
    #                     'data': {},
    #                 })

           
    #         serializer = VerifyAccountSerializer(data=data)
    #         if serializer.is_valid():
    #             email = serializer.data['email']
    #             otp = serializer.data['otp']
    #             user = CustomUser.objects.get(email=email).first()

                
    #             if user.otp_code != otp:
    #                 return Response({
    #                     'status': 400,
    #                     'message': 'Wrong OTP',
    #                     'data': {},
    #                 })

    #             user.is_verified = True
    #             user.save()

    #             return Response({
    #                 'status': 200,
    #                 'message': 'Account Verified',
    #                 'data': {},
    #             })

    #         return Response({
    #             'status': 400,
    #             'message': 'Something went wrong',
    #             'data': serializer.errors,
    #         })

    #     except Exception as e:
    #         print(e)


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

                

                return Response({
                    'status': 200,
                    'message': 'Login successful',
                    'data': {},
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


# class RegisterViewsets(APIView):
#     def post(self, request):
#         try:
#             data = request.data
#             serializer = CustomUserSerializer(data=data)
#             if serializer.is_valid():
#                 serializer.save()
#                 send_otp_via_email(serializer.data['email'])
#                 return Response({
#                     'status': 200,
#                     'message': 'Registration successful. Check your email for verification.',
#                     'data': serializer.data,
#                 })
#             return Response({
#                 'status': 400,
#                 'message': 'Something went wrong',
#                 'data': serializer.errors,
#             })

#         except Exception as e:
#             print(e)

#     def get(self, request):
#         users = CustomUser.objects.all()
#         serializer = CustomUserSerializer(users, many=True)
#         return Response({
#             'status': 200,
#             'message': 'User list retrieved successfully',
#             'data': serializer.data,
#         })


# class VerifyOtpViewsets(APIView):
#     def post(self, request):
#         try:
#             data = request.data
#             serializer = VerifyAccountSerializer(data=data)
#             if serializer.is_valid():
#                 email = serializer.data['email']
#                 otp = serializer.data['otp']
#                 user = CustomUser.objects.filter(email=email).first()

#                 if not user:
#                     return Response({
#                         'status': 400,
#                         'message': 'Invalid email',
#                         'data': {},
#                     })

#                 if user.otp_code != otp:
#                     return Response({
#                         'status': 400,
#                         'message': 'Wrong OTP',
#                         'data': {},
#                     })

#                 user.is_verified = True
#                 user.save()

#                 return Response({
#                     'status': 200,
#                     'message': 'Account Verified',
#                     'data': {},
#                 })

#             return Response({
#                 'status': 400,
#                 'message': 'Something went wrong',
#                 'data': serializer.errors,
#             })

#         except Exception as e:
#             print(e)


# class LoginViewsets(APIView):
#     def post(self, request):
#         try:
#             data = request.data
#             serializer = LoginSerializer(data=data)
#             if serializer.is_valid():
#                 email = serializer.data['email']
#                 password = serializer.data['password']
#                 user = authenticate(request, email=email, password=password)

#                 if user is None:
#                     return Response({
#                         'status': 400,
#                         'message': 'Invalid credentials',
#                         'data': {},
#                     })

#                 if not user.is_verified:
#                     return Response({
#                         'status': 400,
#                         'message': 'Account is not verified',
#                         'data': {},
#                     })

                

#                 return Response({
#                     'status': 200,
#                     'message': 'Login successful',
#                     'data': {},
#                 })

#             return Response({
#                 'status': 400,
#                 'message': 'Something went wrong',
#                 'data': serializer.errors,
#             })

#         except Exception as e:
#             print(e)

#     def get(self, request):
       
#         return Response({
#             'status': 200,
#             'message': 'GET request handled',
#             'data': {},
#         })


# from django.contrib.auth.models import User
# from django.contrib import messages
# from django.utils import timezone
# from django.core.mail import send_mail
# from django.contrib.auth import authenticate,login,logout,get_user_model
# # from django.views import View

# User = get_user_model()


# class RegisterViewsets(viewsets.ModelViewSet):
#     def post(self, request):
#         try:
#             data= request.data
#             serializers = CustomUserSerializer(data=data)

#             if serializers.is_valid():
#                 serializers.save()
#                 send_otp_via_email(serializers.data ['email'])
#                 return Response({
#                     'message' : 'Check your email to verify',
#                     'data' : serializers.data

#                 })
            
#             else:
#                 return Response({
#                     'message' : 'Check your email to verify',
#                    'data' : serializers.data

#                 })


#         except Exception as e:
#             print(e)

# class VerifyOtpViewsets(viewsets.ModelViewSet):
#         def post(self,request):





# class index(View):
#     def get(self, request):
#         return render(request, 'index.html')



# #-------For Email OTP--------#
    
    # form_class = RegisterForm

    # def get(self, request):
    #     form = self.form_class()
    #     return render(request, self.template_name, {'form': form})

#     def post(self, request):
        

#         serializers = self.serializer_class(request.POST)

#         try:

#             if serializers.is_valid():
#                 serializers.save()
#                 send_mail(serializers.data ['email'])
#                 return Response({
#                      'message' : 'Check your email to verify',
#                      'data' : serializers.data

#                  })

            
#             else:
#                 return Response({
#                      'message' : 'Check your email to verify',
#                     '   data' : serializers.data

#                  })


#         except Exception as e:
#              print(e)
    

# class VerifyViewsets(viewsets.ModelViewSet):
#     serializer_class = OtpTokenSerializer  

#     def get(self, request, username):
#         try:
#             user = get_user_model().objects.get(username=username)
#             user_otp = OtpToken.objects.filter(user=user).last()
            
#         except get_user_model().DoesNotExist:
#             messages.error(request, "User not found.")
            

#     def post(self, request, username):
#         try:
#             user = get_user_model().objects.get(username=username)
#             user_otp = OtpToken.objects.filter(user=user).last()
            
#             if user_otp.otp_expires_at > timezone.now():
#                 user.is_active = True
#                 user.save()
#                 messages.success(request, "Account activated successfully!! Processed Login.")
                
#             else:
#                 messages.warning(request, "The OTP has expired. Get a new OTP.")
               
#         except get_user_model().DoesNotExist:
#             messages.error(request, "User not found.")
            
#         except OtpToken.DoesNotExist:
#             messages.error(request, "No OTP found for the user.")
            

        # messages.warning(request, "Invalid OTP entered. Enter a valid OTP!")
        # return redirect("verify-email", username=user.username)
    
        




# class resend_otp(View):
#     template_name = "resend_otp.html"


#     def post(self,request):
    
#         user_email = request.POST["otp_email"]
        
#         try:
#             user = get_user_model().objects.get(email=user_email)
#             otp = OtpToken.objects.create(user=user, otp_expires_at=timezone.now() + timezone.timedelta(minutes=5))
            
            
          
#             subject="Email Verification"
#             message = f"""
#                                 Hi {user.username}, here is your OTP {otp.otp_code} 
#                                 it expires in 5 minute, use the url below to redirect back to the website
#                                 http://127.0.0.1:8000/verify-email/{user.username}
                                
#                                 """
#             sender = "Pratik.thapa.1223@gmail.com"
#             receiver = [user.email, ]
        
        
            
#             send_mail(
#                     subject,
#                     message,
#                     sender,
#                     receiver,
#                     fail_silently=False,
#                 )
            
#             messages.success(request, "Enter your email-address again to get OTP")
#             return redirect("verify-email", username=user.username)

#         except get_user_model().DoesNotExist:
#             messages.warning(request, "This email dosen't exist in the database")
#             return redirect("resend-otp")
        
#     def get(self,request):      
#         context = {}

#         return render(request, self.template_name, context)




# class SigninViewsets(viewsets.ModelViewSet):
#     serializer_class = 
    
#     def post(self, request):
           
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
        
#         if user is not None:    
#             login(request, user)
#             messages.success(request, f"Hi {request.user.username}, you are now logged-in")
#             # return redirect(home.as_view())
        
#         else:
#             messages.warning(request, "Invalid credentials")
#             return redirect("signin")
        
#     def get(self, request):
            
#         return render(request, self.template_name, )
    
    

# def login(request):
    
#     return render(request, 'dashboard/login.html')
# def code(request):
    
#     return render(request, 'dashboard/code.html')

# def logout(request):
    
#     pass




