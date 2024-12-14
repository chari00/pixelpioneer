# accountsapi/urls.py
from django.urls import path
from .views import loginpost, RegisterView, ProfileView, generate_otp_for_email, verify_otp_login, verify_registration_otp

urlpatterns = [
    path('login', loginpost, name='login_post'),
    path('signup', RegisterView.as_view()),
    path('profile', ProfileView.as_view()),
    path('generate-otp/<str:email>/', generate_otp_for_email, name='generate_otp'),
    path('verify-otp-login', verify_otp_login, name='verify_otp_login'),
    path('verify-registration', verify_registration_otp, name='verify_registration'),
]
