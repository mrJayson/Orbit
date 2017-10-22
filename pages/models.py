from ckeditor.fields import RichTextField
from django.db import models
from django.urls import reverse
from model_utils.models import SoftDeletableModel
import uuid
import uuslug
from accounts.models import Account
from .managers import PageManager


class Page(SoftDeletableModel):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    content = RichTextField(blank=True)
    author = models.ForeignKey(Account)
    creation_date = models.DateTimeField(auto_now_add=True)
    group_id = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    version = models.IntegerField()
    changelog = models.CharField(max_length=50, blank=True)
    objects = PageManager()

    def get_absolute_url(self):
        return reverse('pages:detail', kwargs={'slug': self.slug})

    def get_absolute_history_url(self):
        return reverse('pages:history', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = self.slugify()
        super(Page, self).save(*args, **kwargs)

    def slugify(self):
        if self.is_removed:
            # append version number to slug to distinguish between versions
            return uuslug.slugify(self.title + '-' + str(self.version))
        else:
            # no version appended means latest version
            return uuslug.slugify(self.title)
