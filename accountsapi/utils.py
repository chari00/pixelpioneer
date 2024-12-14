# accountsapi/utils.py
import pyotp
from django.core.mail import send_mail
from django.conf import settings

from datetime import datetime, timedelta
from .models import OTP


# def generate_otp(user_email):
#     totp = pyotp.TOTP('base32secret3232')
#     otp = totp.now()
    
#     subject = "Your OTP Code"
#     message = f"Hello, here is your OTP: {otp}"
#     from_email = settings.DEFAULT_FROM_EMAIL
#     send_mail(subject, message, from_email, [user_email])
#     return otp


def generate_otp(user):
    totp = pyotp.TOTP('base32secret3232')
    otp_code = totp.now()
    
    # Store OTP in database
    OTP.objects.create(
        user=user,
        otp=otp_code,
        expires_at=datetime.now() + timedelta(minutes=10)
    )
    
    subject = "Your OTP Code"
    message = f"Hello, here is your OTP: {otp_code}"
    from_email = settings.DEFAULT_FROM_EMAIL
    send_mail(subject, message, from_email, [user.email])
    return otp_code