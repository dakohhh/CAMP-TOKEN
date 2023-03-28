from django.db import models
from django.contrib.auth.models import AbstractUser

from . import utils

# Create your models here.
# from django.contrib.auth.models import User




class CustomUser(AbstractUser):
    username = models.CharField(max_length=30, blank=True, null=True)
    
    email = models.EmailField(unique=True, null=False)

    wallet_id = models.IntegerField(unique=True, default=utils.generate_number(10))

    phone_number = models.IntegerField(unique=True, null=False)

    business_name = models.CharField(max_length=200, null=True)

    business_id = models.CharField(max_length=200, unique=True ,null=False)

    balance = models.FloatField(default=0)

    is_student = models.BooleanField(default=False)

    is_merchant = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    


