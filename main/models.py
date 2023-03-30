from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.



class CustomUser(AbstractUser):
            
    first_name = models.CharField(max_length=100, blank=True, null=True)

    last_name = models.CharField(max_length=100, blank=True, null=True)

    username = models.CharField(max_length=30, blank=True, null=True)
    
    email = models.EmailField(unique=True, null=False)

    wallet_id = models.IntegerField(unique=True, null=False)

    phone_number = models.IntegerField(unique=True, null=False)

    business_name = models.CharField(max_length=200, null=True)

    business_id = models.CharField(max_length=200, unique=True ,null=True)

    balance = models.FloatField(default=0)
    
    transaction_pin = models.CharField(max_length=6, null=True)

    is_student = models.BooleanField(default=False)

    is_merchant = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


