from multiprocessing.sharedctypes import Value
from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ngettext_lazy as _
from django.core.exceptions import ValidationError

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_("Email is required"))

        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)

        user.set_password(password)

        user.save()

        return user

    def create_superuser(self, email, password, **extra_fields):
        # is_staff = models.BooleanField(default=True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("SuperUser should have is_staff as True")

        if extra_fields.get('is_active') is not True:
            raise ValueError('SuperUser must have is_active True')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('SuperUser must have is_superuser True')

        return self.create_user(email, password, **extra_fields)

def validate_min(value):
    if len(value)<10:
        raise ValidationError(
            _('Must contain at least 10 digit'),
            params={'value':value},
        )

class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    phone_number = models.CharField(null=False, validators=[validate_min], unique=True, max_length=14)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username', 'phone_number']

    objects = CustomUserManager()

    def __str__(self):
        return f"User {self.email}"