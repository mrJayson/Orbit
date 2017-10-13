from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class Account(AbstractUser):
    # Inherits from AbstractUser which already has attributes:
    # username
    # first_name
    # last_name
    # email
    # is_staff
    # is_active
    # date_joined

    bio = models.TextField(blank=True)

    def get_absolute_url(self):
        return reverse('accounts:detail', kwargs={'pk': self.pk})

    @property
    def full_name(self):
        return self.first_name + ' ' + self.last_name
