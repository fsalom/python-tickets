from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(blank=True, null=True, unique=True, verbose_name="Email")
    first_name = models.CharField(max_length=150, null=True)