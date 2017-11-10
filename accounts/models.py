from django.db import models
from django.contrib.auth.models import AbstractUser, Permission
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from guardian.shortcuts import assign_perm


class Account(AbstractUser):
    # Inherits from AbstractUser which already has attributes:
    # username
    # first_name
    # last_name
    # email
    # is_staff
    # is_active
    # date_joined

    location = models.CharField(
        max_length=64,
        blank=True,
        help_text=_("Which part of Western Sydney are you from?")
    )
    education = models.CharField(
        max_length=64,
        blank=True,
        help_text=_("Where are you currently studying?")
    )
    bio = models.TextField(
        blank=True,
        help_text=_("Tell us a bit about yourself")
    )

    def get_absolute_url(self):
        return reverse('accounts:detail', kwargs={'pk': self.pk})

    @property
    def full_name(self):
        return (self.first_name + ' ' + self.last_name).strip()

    def save(self, *args, **kwargs):
        super(Account, self).save(*args, **kwargs)
        # Give permission to self to edit own profile
        content_type = ContentType.objects.get_for_model(self)
        edit_perm, created = Permission.objects.get_or_create(codename='change_account', content_type=content_type)
        if created:
            assign_perm(edit_perm, self, self)
