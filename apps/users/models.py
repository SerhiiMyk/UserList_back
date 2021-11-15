from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.core import validators as V

from apps.users.managers import UserManager


class UserModel(AbstractBaseUser):
    class Meta:
        db_table = 'auth_user'

    username = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=128, unique=True)
    password = models.CharField(max_length=128, verbose_name='password')
    user_type = models.CharField(max_length=20)

    USERNAME_FIELD = 'username'
    objects = UserManager()
