from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

from spotcrew_backend.images.models import Image


class User(AbstractBaseUser):
    type = models.TextField()
    avatar_id = models.OneToOneField(Image, models.DO_NOTHING, db_column="image_id")
