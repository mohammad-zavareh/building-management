from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

from datetime import timedelta, datetime


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, phone_number, password, **extra_fields):
        """Create and save a User with the given phone number and password."""
        if not phone_number:
            raise ValueError('The given phone_number must be set')
        # phone_number = self.normalize_phone_number(phone_number)
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone_number, password=None, **extra_fields):
        """Create and save a regular User with the given phone_number and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phone_number, password, **extra_fields)

    def create_superuser(self, phone_number, password, **extra_fields):
        """Create and save a SuperUser with the given phone_number and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(phone_number, password, **extra_fields)


class User(AbstractUser):
    username = None
    phone_number = models.IntegerField(unique=True, verbose_name='شماره همراه')

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return str(self.phone_number)


class Otp(models.Model):
    phone_number = models.IntegerField(unique=True)
    code = models.IntegerField()
    created = models.DateTimeField()

    def get_expire_time(self):
        time_to_expire = 1
        created_time = self.created.replace(tzinfo=None)

        expire_time = created_time + timedelta(minutes=time_to_expire)

        now = datetime.now()
        if expire_time > now:
            time_reverse = expire_time - now
            time_reverse_seconds = time_reverse.seconds
        else:
            time_reverse_seconds = 0

        return time_reverse_seconds