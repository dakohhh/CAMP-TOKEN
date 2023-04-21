from datetime import datetime
from django.db import transaction
from django.http import HttpRequest
from django.core.exceptions import ValidationError
from Transactions.models import Transactions
from main.models import CustomUser
from Verification.models import VerificationToken
from utils.shortcuts import generate_transaction_id, get_object_or_none




def save_verifcation_token(email:str,token:str, expiration_time:datetime):

    verification = VerificationToken(user_email=email, token=token, expiration_time=expiration_time)

    verification.save()


def update_verication_token(email, token:str, expiration_time:datetime):

    verification = get_object_or_none(VerificationToken, email=email)

    verification.token = token
    
    verification.expiration_time = expiration_time

    verification.save()



def delete_verfication_token(token):
    token_obj = get_object_or_none(VerificationToken, token=token)


    if token: token_obj.delete()


def update_user(email, transaction_pin:int=None, status=True):
    user = get_object_or_none(CustomUser, email=email)

    user.is_verified = status

    user.transaction_pin = transaction_pin
    
    user.save()


@transaction.atomic
def pay_merchant_transaction(request:HttpRequest, merchant:CustomUser, amount:int, transaction_id:str):
    # - START TRANSACTION LOOP

    try:
        with transaction.atomic():
        
            request.user.balance -= amount

            request.user.save()

            merchant.balance += amount

            merchant.save()

            Transactions.objects.create(transaction_id=transaction_id, sender=request.user, recipient=merchant, amount=amount, status=1, type=1)

    except ValidationError:

        Transactions.objects.create(transaction_id=transaction_id, sender=request.user, recipient=merchant, amount=amount, status=0, type=1)



@transaction.atomic
def refund_student_transaction(request:HttpRequest, _transaction:Transactions, refund_transaction_id:str):
    # - START TRANSACTION LOOP
    
    try:
        with transaction.atomic():
        
            request.user.balance -= float(_transaction.amount)

            request.user.save()

            _transaction.sender.balance += float(_transaction.amount)

            _transaction.sender.save()

            _transaction.was_refunded = True

            _transaction.save()

            Transactions.objects.create(transaction_id=refund_transaction_id, sender=_transaction.sender, recipient=request.user, amount=_transaction.amount, status=1, type=2)

    except ValidationError:
        Transactions.objects.create(transaction_id=refund_transaction_id, sender=_transaction.sender, recipient=request.user, amount=_transaction.amount, status=0, type=2)





