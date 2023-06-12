import os
import shutil
import urllib
from io import BytesIO

from PIL import Image
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from .managers import CustomUserManager


def get_default_image():
    return 'default/image.jpg'

def generate_filename(instance):
    user_id = instance.id
    new_filename = f"image_{user_id}.jpg"
    new_filepath = os.path.join("images", new_filename)

    return new_filepath


class User(AbstractUser):
    email = models.EmailField(unique=True)
    nickname = models.CharField(max_length=125, unique=True)
    avatar = models.ImageField(upload_to=generate_filename, default=get_default_image)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["nickname"]

    # groups = models.ManyToManyField(Group, related_name='custom_user_groups')
    # user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions')

    objects = CustomUserManager()






