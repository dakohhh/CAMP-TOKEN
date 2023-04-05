from django.db.models import Model
from typing  import Type
from main.models import CustomUser



def get_object_or_none(klass:Type[Model], *args, **kwargs):
    try:
        return klass.objects.get(*args, **kwargs)
    except klass.DoesNotExist:
        return None
    



