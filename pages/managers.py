from django.db import models
from model_utils.managers import InheritanceManagerMixin, SoftDeletableManagerMixin


class PageManager(InheritanceManagerMixin, SoftDeletableManagerMixin, models.Manager):
    pass
