from django.db import models
from django.contrib.auth.models import AbstractUser

class Account(AbstractUser):
    # Inherits from AbstractUser which already has attributes:
    # username
    # first_name
    # last_name
    # email
    # is_staff
    # is_active
    # date_joined

    bio = models.TextField()
