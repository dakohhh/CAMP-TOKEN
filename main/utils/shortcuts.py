from collections import OrderedDict
from django.db.models import Model
from main.models import CustomUser, Transactions
from secrets import token_hex
from typing  import Type
from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from typing import Union



def get_object_or_none(klass:Type[Model], *args, **kwargs)-> Union[CustomUser, Transactions]:
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


def generate_transaction_id(length):
    
    return token_hex(length)


def is_student(user:User):

    return user.is_student == True


def is_merchant(user:User):
    
    return user.is_student == True