from django.db.models import Model
from main.models import CustomUser, Transactions
from secrets import token_hex
from typing  import Type
from django.contrib.auth.models import User
from typing import Union



def get_object_or_none(klass:Type[Model], *args, **kwargs)-> Union[CustomUser, Transactions]:
    try:
        return klass.objects.get(*args, **kwargs)
    except klass.DoesNotExist:
        return None
    


def does_object_exists(klass:Type[Model], *args, **kwargs)->bool:
    
    return klass.objects.exists(*args, **kwargs)




def generate_transaction_id(length):
    
    return token_hex(length)


def is_student(user:User):

    return user.is_student == True


def is_merchant(user:User):
    
    return user.is_student == True