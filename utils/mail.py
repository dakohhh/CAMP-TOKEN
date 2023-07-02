from typing import Union
from base64 import urlsafe_b64encode, urlsafe_b64decode
from django.conf import settings
from django.core.mail import send_mail
from django.utils.encoding import force_bytes, force_str
from django.http.request import HttpRequest
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from utils.crud import fetchone
from user.models import User



class EmailVerificationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
                str(user.is_active) + str(user.pk) + str(timestamp)
        )


email_verification = EmailVerificationTokenGenerator()


def send_verification_mail(request:HttpRequest, user:User):

    current_site = get_current_site(request)


    token = email_verification.make_token(user)

    encoded_user = urlsafe_b64encode(force_bytes(user.pk))

    verification_url = f'http://{current_site.domain}/accounts/verify/{encoded_user}/{token}'


    send_mail(
        "Verification for Camptoken User", 
        f"Hi {user.first_name} {user.last_name}, please verify your account with this link\n{verification_url}", 
        from_email=settings.EMAIL_HOST_USER, 
        recipient_list=[user.email]
        )




def get_user_from_email_verification_token(uidb64, token: str) -> Union[User, None]:

    try:
        user_id = force_str(urlsafe_b64decode(uidb64))

        user = fetchone(User, pk=user_id)

    except (User.DoesNotExist , TypeError, ValueError, OverflowError):
        return None
    
    if user is not None and email_verification.check_token(user, token):

        return user

    return None

