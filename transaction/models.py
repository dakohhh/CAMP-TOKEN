from django.db import models

from user.models import User

# Create your models here.





class Transactions(models.Model):

    SENT = 1

    REFUNDED = 2

    SUCCESS  = 1

    FAILED = 0

    

    _TRANSACTION_TYPES = [
        (SENT, 'Sent'),
        (REFUNDED, 'Refunded'),
    ]

    _TRANSACTION_STATUS = [
        (SUCCESS, "Success"),
        (FAILED, "Failed"),         
    ]

    transaction_id = models.CharField(max_length=30, primary_key=True, blank=True)

    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender_transactions')

    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipient_transactions')

    amount = models.DecimalField(max_digits=10, null=False,  decimal_places=2)

    transaction_type = models.SmallIntegerField(choices=_TRANSACTION_TYPES)

    transaction_status = models.SmallIntegerField(choices=_TRANSACTION_STATUS)

    was_refunded = models.BooleanField(default=False)

    initiated_by_student = models.BooleanField(default=True)

    date_added = models.DateTimeField(auto_now_add=True, null=False)


    def to_dict(self):
        return {
            "transaction_id": self.transaction_id,
            "sender": f'{self.sender.first_name} {self.sender.last_name}',
            "recipient": f'{self.recipient.business_name}', 
            "amount": self.amount, 
            "transaction_type": self.transaction_type, 
            "transaction_status": self.transaction_status, 
            "was_refunded": self.was_refunded, 
            "date_added": self.date_added
        }