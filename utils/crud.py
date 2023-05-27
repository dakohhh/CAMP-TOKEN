from typing import List, Type, Union
from django.http import HttpRequest
from django.db import transaction
from django.db.models import Model
from django.core.exceptions import ValidationError
from transaction.models import Transactions
from user.models import User




def fetchone(klass:Type[Model], *args, **kwargs)-> Union[User, None]:
    try:
        return klass.objects.get(*args, **kwargs)
    except klass.DoesNotExist:
        return None
    except Exception as e:
        raise e


def fetchall(klass:Type[Model], *args, **kwargs)-> Union[List[User], None]:
    try:
        return klass.objects(*args, **kwargs)
    except klass.DoesNotExist:
        return None
    except Exception as e:
        raise e
    

@transaction.atomic
def pay_merchant_transaction(request:HttpRequest, merchant:User, amount:int, transaction_id:str):
    # - START TRANSACTION LOOP
    try:
        with transaction.atomic():
        
            request.user.balance -= amount

            request.user.save()

            merchant.balance += amount

            merchant.save()

            new_transaction = Transactions(transaction_id=transaction_id, sender=request.user, recipient=merchant, amount=amount, transaction_status=Transactions.SUCCESS, transaction_type=Transactions.SENT)

            new_transaction.save()

            return new_transaction

    except:

        failed_transaction = Transactions(transaction_id=transaction_id, sender=request.user, recipient=merchant, amount=amount, transaction_status=Transactions.FAILED, transaction_type=Transactions.SENT)

        return failed_transaction