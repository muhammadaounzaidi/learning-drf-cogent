from django.contrib.auth.models import AbstractUser
from django.db import models
from .manager import  UserManager
from django_extensions.db.models import TimeStampedModel

# Create your models here.
class User(AbstractUser,TimeStampedModel):
    email = models.EmailField(unique=True)
    username = None
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = UserManager()

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.email
