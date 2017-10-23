from django.db import models
from django.db.models.query import QuerySet
from model_utils.managers import InheritanceManagerMixin, InheritanceQuerySetMixin, SoftDeletableQuerySetMixin


class PageQuerySet(SoftDeletableQuerySetMixin, InheritanceQuerySetMixin, QuerySet):
    pass


class PageManager(InheritanceManagerMixin, models.Manager):
    _queryset_class = PageQuerySet
