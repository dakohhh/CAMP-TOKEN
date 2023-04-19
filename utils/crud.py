from datetime import datetime
from main.models import CustomUser
from Verification.models import VerificationToken
from utils.shortcuts import get_object_or_none



def save_verifcation_token(email:str,token:str, expiration_time:datetime):

    verification = VerificationToken(user_email=email, token=token, expiration_time=expiration_time)

    verification.save()





def delete_verfication_token(token):
    token_obj = get_object_or_none(VerificationToken, token=token)


    if token: token_obj.delete()


def update_user_verication(email, status=True):
    user = get_object_or_none(CustomUser, email=email)

    user.is_verified = status
    
    user.save()




