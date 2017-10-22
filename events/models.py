from django.db import models
from django.urls import reverse
from django.utils.timesince import timesince
from model_utils.models import TimeFramedModel
from pages.models import Page


class Event(Page, TimeFramedModel):
    start = models.DateTimeField()
    end = models.DateTimeField()
    # attendance = models.ManyToManyField(Account)

    # TODO ensure start is before end

    @property
    def duration(self):
        return timesince(d=self.start, now=self.end)

    @property
    def display_date_range(self):
        if self.start.month == self.end.month and self.start.day == self.end.day:
            return self.start.strftime('%d %b')
        else:
            return self.start.strftime('%d %b') + ' - ' + self.end.strftime('%d %b')

    @property
    def display_date_time_range(self):
        return self.start.strftime('%Y, %b %d, %I:%M%p') + ' - ' + self.end.strftime('%Y, %b %d, %I:%M%p')

    def get_absolute_url(self):
        return reverse('events:detail', kwargs={'slug': self.slug})

    def get_absolute_history_url(self):
        return reverse('events:history', kwargs={'slug': self.slug})
