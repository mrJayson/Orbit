from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
