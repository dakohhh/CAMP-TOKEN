from django.db import models
from django.utils import timezone

# Create your models here.





class VerificationToken(models.Model):

    user_email =models.EmailField()
    token = models.CharField(max_length=64, unique=True)
    expiration_time = models.DateTimeField()


    def is_token_expired(self) -> bool:
        return timezone.now() > self.expiration_time
