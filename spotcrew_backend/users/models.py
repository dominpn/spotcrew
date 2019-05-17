from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True, null=False)
    username = models.CharField(unique=True, null=False, max_length=40)
    date_joined = models.DateTimeField(default=timezone.now, null=True)
    is_active = models.BooleanField(default=False)
    avatar_link = models.TextField(null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        managed = True

# https://medium.com/@apogiatzis/create-a-restful-api-with-users-and-jwt-authentication-using-django-1-11-drf-part-1-288268602bb7
