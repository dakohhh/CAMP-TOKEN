from django.db import models

from main.models import CustomUser



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



"""
FOR STATUS ->
    1 FOR SUCCESS
    2 FOR FAILED
    3 FOR PENDING

FOR TYPE

"""