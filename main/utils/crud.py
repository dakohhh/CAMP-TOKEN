from main.models import VerificationToken
from datetime import datetime



def save_verifcation_token(email:str,token:str, expiration_time:datetime):

    verification = VerificationToken(user_email=email, token=token, expiration_time=expiration_time)

    verification.save()

