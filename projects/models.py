from django.db import models
from django.urls import reverse
from pages.models import Page


class Project(Page):

    def get_absolute_url(self):
        return reverse('projects:detail', kwargs={'slug': self.slug})
