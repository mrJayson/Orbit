from django.db import models
from django.urls import reverse
from uuslug import uuslug
from accounts.models import Account
from pages.models import Page


class Meeting(Page):
    start = models.DateTimeField()
    end = models.DateTimeField()
    # attendance = models.ManyToManyField(Account)

    # TODO ensure start is before end

    @property
    def display_date_range(self):
        if self.start.month == self.end.month and self.start.day == self.end.day:
            return self.start.strftime('%d %b')
        else:
            return self.start.strftime('%d %b') + ' - ' + self.end.strftime('%d %b')

    def get_absolute_url(self):
        return reverse('meetings:detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = uuslug(self.title, instance=self)
        super(Meeting, self).save(*args, **kwargs)
