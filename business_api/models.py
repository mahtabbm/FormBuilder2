
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.conf import settings


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


class BusinessFeedItem(models.Model):
    """Business status update"""
    business = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 on_delete=models.CASCADE)
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status_text


class Form(models.Model):
    title = models.CharField(max_length=255, default='untitled form')
    description = models.CharField(max_length=550, default='description')

    business = models.ForeignKey(Business, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Part(models.Model):
    title = models.CharField(max_length=255, default='untitled part')
    description = models.CharField(max_length=500, default='Part Specification')

    is_char = models.BooleanField(default=False)
    is_int = models.BooleanField(default=False)
    is_datetime = models.BooleanField(default=False)
    is_file = models.BooleanField(default=False)
    is_decimal = models.BooleanField(default=False)
    is_date = models.BooleanField(default=False)

    form = models.ForeignKey(Form, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Option(models.Model):
    title = models.CharField(max_length=255, default='new option')
    is_required = models.BooleanField(default=False)

    text_field = models.CharField(max_length=255, default='text')
    number_field = models.IntegerField(default=0)
    decimal_field = models.DecimalField(max_digits=5, decimal_places=2)
    datetime_field = models.DateTimeField(auto_now_add=True)
    file_field = models.FileField()
    date_field = models.DateField(auto_now_add=True)

    part = models.ForeignKey(Part, on_delete=models.CASCADE)

    def __str__(self):
        return self.title







