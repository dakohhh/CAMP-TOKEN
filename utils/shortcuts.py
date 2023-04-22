from secrets import token_hex
from typing  import Type
from typing import Union
from collections import OrderedDict
from django.db.models import Model
from django.http import Http404, HttpResponse, HttpResponseForbidden
from django.http.request import HttpRequest
from django.db.models.query import QuerySet
from main.models import CustomUser
from Transactions.models import Transactions
from Verification.models import VerificationToken


def get_object_or_none(klass:Type[Model], *args, **kwargs)-> Union[CustomUser, Transactions, VerificationToken, None]:
    try:
        return klass.objects.get(*args, **kwargs)
    except klass.DoesNotExist:
        return None
    
    


def does_object_exists(klass:Type[Model], *args, **kwargs)-> bool:
    
    return klass.objects.exists(*args, **kwargs)



def group_transactions_by_date(trans_history:QuerySet[Transactions])-> dict:

    transactions_by_date = OrderedDict()
  
    for transaction in trans_history:
        if len(transactions_by_date) == 0:
            transactions_by_date[transaction.date_added.date().strftime("%B %d %Y")] = [transaction]
        else:
            if transaction.date_added.date().strftime("%B %d %Y") in transactions_by_date:
                transactions_by_date[transaction.date_added.date().strftime("%B %d %Y")].append(transaction)
            else:
                transactions_by_date[transaction.date_added.date().strftime("%B %d %Y")] = [transaction]

    return transactions_by_date



def forbidden_if_merchant(view_func):
    def wrapper(request:HttpRequest, *args, **kwargs):

        if request.user.is_merchant:
            return HttpResponseForbidden("You do not have permission to access this page, forbidden for merchants")
        
        return view_func(request, *args, **kwargs)

    return wrapper


def forbidden_if_student(view_func):
    def wrapper(request:HttpRequest, *args, **kwargs):

        if request.user.is_student:
            return HttpResponseForbidden("You do not have permission to access this page, forbidden for students")
        
        return view_func(request, *args, **kwargs)

    return wrapper


def forbidden_if_already_refunded(view_func):
    def wrapper(request:HttpRequest, transaction_id:str,  *args, **kwargs):
        
        transaction = get_object_or_none(Transactions, transaction_id=transaction_id)

        if not transaction:
            return HttpResponse("Page not found", status=404)

        if transaction.was_refunded or transaction.type ==2:
            return HttpResponseForbidden("Refund has already been made")
        
        return view_func(request, transaction_id, *args, **kwargs)

    return wrapper



def get_verification_url(request:HttpRequest, email:str, verification_token:str):

    base_url = request.build_absolute_uri("/")[:-1]

    return f"{base_url}/accounts/verify?email={email}&token={verification_token}"




def is_valid_verification(email:str, token:str) -> bool :

    verification = get_object_or_none(VerificationToken, user_email=email, token=token)

    if verification !=  None and (not verification.is_token_expired()):
        return True
    else:
        return False


def generate_transaction_id(length:int):
    
    return token_hex(length)

