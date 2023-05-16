from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager




class UserProfileManager(BaseUserManager):
    def _create_user(self, email, password, first_name, last_name, phone_number, **extra_fields):

        """ Create a new user profile """

        if not email:
            raise ValueError('User must have an email address')
        
        if not password:
            raise ValueError("Password must be provided")

        email = self.normalize_email(email)

        user = self.model(
            email=self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            phone_number = phone_number,
            **extra_fields
        )

        user.set_password(password)

        user.save(using=self._db)

        return user
    

    
    def create_user(self, email, password, first_name, last_name, phone_number, **extra_fields):

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_superuser", False)

        return self._create_user(email, password, first_name, last_name, phone_number, **extra_fields)
    
    def create_superuser(self, email, password, first_name, last_name, phone_number, **extra_fields):

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_superuser", True)

        return self._create_user(email, password, first_name, last_name, phone_number, **extra_fields)



class CustomUser(AbstractUser, PermissionsMixin):
            
    first_name = models.CharField(max_length=100, blank=True, null=True)

    last_name = models.CharField(max_length=100, blank=True, null=True)
    
    email = models.EmailField(db_index=True, unique=True, null=False)

    wallet_id = models.IntegerField(unique=True, null=False)

    phone_number = models.IntegerField(unique=True, null=False)

    business_name = models.CharField(max_length=200, null=True)

    business_id = models.CharField(max_length=200, unique=True ,null=True)

    balance = models.FloatField(default=0)
    
    transaction_pin = models.CharField(max_length=6, null=True)

    is_student = models.BooleanField(default=False)

    is_verified = models.BooleanField(default=False)

    is_merchant = models.BooleanField(default=False)


    is_staff = models.BooleanField(default=True)

    is_active = models.BooleanField(default=True)

    is_superuser = models.BooleanField(default=False)


    objects = UserProfileManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ["first_name", "last_name", "phone_number"]













