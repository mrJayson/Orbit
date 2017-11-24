from django.db import models
from django.urls import reverse
from pages.models import Page


class Project(Page):
    deadline = models.DateTimeField(blank=True, null=True)
    code = models.CharField(max_length=5, unique=True)

    to_do = 0
    in_progress = 1
    completed = 2
    columns = (
        (to_do, 'to_do'),
        (in_progress, 'in_progress'),
        (completed, 'completed'),
    )

    def get_absolute_url(self):
        return reverse('projects:detail', kwargs={'slug': self.slug})

    def get_absolute_board_url(self):
        return reverse('projects:board', kwargs={'slug': self.slug})


class Task(Page):
    task_project = models.ForeignKey(Project)
    column = models.CharField(max_length=1, choices=Project.columns, default=0)
    code = models.PositiveSmallIntegerField(unique=True)

    class Meta:
        unique_together = ('task_project', 'code')

    def get_absolute_url(self):
        project_slug = self.task_project.slug
        task_slug = self.slug
        return reverse('projects:task_detail', kwargs={'project_slug': project_slug, 'task_slug': task_slug})
