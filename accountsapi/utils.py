# accountsapi/utils.py
import pyotp
from django.core.mail import send_mail
from django.conf import settings

def generate_otp(user_email):
    totp = pyotp.TOTP('base32secret3232')
    otp = totp.now()
    
    subject = "Your OTP Code"
    message = f"Hello, here is your OTP: {otp}"
    from_email = settings.DEFAULT_FROM_EMAIL
    send_mail(subject, message, from_email, [user_email])
    return otp
