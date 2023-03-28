from django.db import models
from django.contrib.auth.models import AbstractUser

from . import utils

# Create your models here.
# from django.contrib.auth.models import User




class User(AbstractUser):
    wallet_id = models.IntegerField(unique=True, default=utils.generate_number(10))
    balance = models.FloatField(default=0)
    is_student = models.BooleanField(default=False)
    is_merchant = models.BooleanField(default=False)

    


