from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from .models import Page


class PageForm(ModelForm):

    error_messages = {
        'password_mismatch': _("The two password fields do not match")
    }

    def __init__(self, author=None, version=None, *args, **kwargs):
        self.author = author
        self.version = version
        super(PageForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Page
        fields = [
            'title',
            'content',
        ]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _("Title goes here..."),
            }),

        }

    def save(self, commit=True):
        page = super(PageForm, self).save(commit=False)
        page.author = self.author
        if self.version is None:
            page.version = 1
        else:
            existing_page = Page.objects.get(pk=page.pk)
            existing_page.is_removed = True
            existing_page.save()

            page.parent = existing_page  # Retain link to previous version
            page.id = None  # Create a new instance, do not override existing instance
            page.pk = None
            page.version = self.version + 1
        if commit:
            page.save()
        return page
