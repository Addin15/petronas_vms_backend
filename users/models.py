from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    first_name = None
    last_name = None
    username =  None
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    password = models.TextField()
    google_token = models.JSONField(default=None, null=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
