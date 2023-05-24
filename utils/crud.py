from typing import List, Type, Union
from user.models import User
from django.db.models import Model



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