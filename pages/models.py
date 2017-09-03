from django.db import models

from uuslug import uuslug

from accounts.models import Account

class Page(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    content = models.TextField(blank=True)
    author = models.ForeignKey(Account)
    creation_date = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True)
    version = models.IntegerField()

    def save(self, *args, **kwargs):
        self.slug = uuslug(self.title, instance=self)
        super(Page, self).save(*args, **kwargs)
