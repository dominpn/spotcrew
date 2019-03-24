from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager
from django.db import models

from images.models import Image


class User(AbstractBaseUser):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True, null=False)
    username = models.CharField(unique=True, null=False, max_length=40)
    password = models.CharField(max_length=128, null=False)
    type = models.TextField(default='normal')
    is_active = models.BooleanField(default=False)
    avatar_id = models.OneToOneField(Image, models.DO_NOTHING, db_column="image_id", null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        managed = True

# https://medium.com/@apogiatzis/create-a-restful-api-with-users-and-jwt-authentication-using-django-1-11-drf-part-1-288268602bb7
