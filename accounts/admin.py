from django.contrib import admin
from accounts.models import CustomUser
# from django.contrib.auth.admin import UserAdmin
admin.site.register(CustomUser)
# admin.site.register(OtpToken)






# from django.contrib import admin
# from .models import CustomUser, OtpToken



# class CustomUserAdmin(UserAdmin):
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('username', 'email', 'password1', 'password2')}
#          ),
#     )


# class OtpTokenAdmin(admin.ModelAdmin):
#     list_display = ("user", "otp_code")


# admin.site.register(OtpToken, OtpTokenAdmin)
 #CustomUserAdmin) 


