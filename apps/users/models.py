from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.core import validators as V

from apps.users.managers import UserManager


class UserModel(AbstractBaseUser):
    class Meta:
        db_table = 'auth_user'

    username = models.CharField(max_length=20, unique=True,
                                validators=[V.MinLengthValidator(2), V.MaxLengthValidator(20)])
    first_name = models.CharField(max_length=20, validators=[V.MinLengthValidator(2), V.MaxLengthValidator(20)])
    last_name = models.CharField(max_length=20, validators=[V.MinLengthValidator(2), V.MaxLengthValidator(20)])
    email = models.EmailField(max_length=128, unique=True)
    password = models.CharField(max_length=128, validators=[V.RegexValidator('^(?=.*\d)(?=.*[a-zA-Z])([^\s]){8,16}$',
                                                                             'Your password must contain at least one digit and one letter')])
    user_type = models.CharField(max_length=20)

    USERNAME_FIELD = 'email'
    objects = UserManager()
