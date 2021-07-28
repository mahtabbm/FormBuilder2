
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models


# Create your models here.
from django.contrib.auth.base_user import BaseUserManager


class BusinessManager(BaseUserManager):
    """manager for business user"""

    def create_user(self, email, password, name=None):
        """create a new user"""
        if not email:
            raise ValueError("Email is Required.")

        if not password:
            raise ValueError("Password is Required.")

        """normalizing email, all in lowercase, avoid case sensitive"""
        email = self.normalize_email(email)
        """creating business model"""
        user = self.model(email=email, name=name)

        """not to store plain text in db"""
        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, name=None):
        user = self.create_user(email, password, name)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user


class Business(AbstractBaseUser, PermissionsMixin):
    """database model for Business User in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = BusinessManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_name(self):
        """RETRIEVE name of the business user"""
        return self.name

    def __str__(self):
        """string representation of the user"""
        return self.email
