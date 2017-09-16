from django.db import models
from accounts.models import Account
from pages.models import Page

class Meeting(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateField()
    notes = models.ForeignKey(Page)
    attendance = models.ManyToManyField(Account)

    class Meta:
        ordering = ['date']
