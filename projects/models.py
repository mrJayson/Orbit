from django.db import models
from django.urls import reverse
from pages.models import Page


class Project(Page):

    deadline = models.DateTimeField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('projects:detail', kwargs={'slug': self.slug})

    def get_absolute_board_url(self):
        return reverse('projects:board', kwargs={'slug': self.slug})
