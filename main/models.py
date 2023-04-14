from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser



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

    is_verified = models.BooleanField(default=False)

    is_merchant = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []






class Transactions(models.Model):

    TRANSACTION_TYPES = (
        (1, 'Sent'),
        (2, 'Refunded'),
    )

    TRANSACTION_STATUS = (
        (1, "Success"),
        (0, "Failed"),         
    )
    transaction_id = models.CharField(max_length=30, primary_key=True, blank=True)

    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sender_transactions')

    recipient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='recipient_transactions')

    amount = models.DecimalField(max_digits=10, null=False,  decimal_places=2)

    type = models.SmallIntegerField(choices=TRANSACTION_TYPES)

    status = models.SmallIntegerField(choices=TRANSACTION_STATUS)

    was_refunded = models.BooleanField(default=False)

    date_added = models.DateTimeField(auto_now_add=True, null=False)



class VerificationToken(models.Model):

    user_email =models.EmailField()
    token = models.CharField(max_length=64, unique=True)
    expiration_time = models.DateTimeField()


    def is_token_expired(self) -> bool:
        return timezone.now() > self.expiration_time



"""
FOR STATUS ->
    1 FOR SUCCESS
    2 FOR FAILED
    3 FOR PENDING

FOR TYPE

"""
