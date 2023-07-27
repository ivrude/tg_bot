from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class Theme(models.Model):
    name = models.CharField(max_length=100)


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_time = models.DateTimeField()
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)


class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, is_admin=False):
        if not phone_number:
            raise ValueError("Users must have a phone number")

        user = self.model(phone_number=phone_number, is_admin=is_admin)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None):
        user = self.create_user(phone_number, password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class Client(AbstractBaseUser):
    phone_number = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=128)  # Замість is_active
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'phone_number'

    def __str__(self):
        return self.phone_number

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
