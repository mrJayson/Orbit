from django.db import models
from accounts.models import Account
from pages.models import Page

class Meeting(Page):
    start = models.DateTimeField()
    end = models.DateTimeField()
    attendance = models.ManyToManyField(Account)

    class Meta:
        ordering = ['start']

        # TODO ensure start is before end
