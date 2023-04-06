from django.db.models import Model
from secrets import token_hex
from typing  import Type



def get_object_or_none(klass:Type[Model], *args, **kwargs):
    try:
        return klass.objects.get(*args, **kwargs)
    except klass.DoesNotExist:
        return None
    





def generate_transaction_id(length):
    
    return token_hex(length)


