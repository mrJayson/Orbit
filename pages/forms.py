from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from .models import Page


class PageForm(ModelForm):

    error_messages = {
        'password_mismatch': _("The two password fields do not match")
    }

    def __init__(self, account=None, *args, **kwargs):
        self.account = account
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
        page.author = self.account
        page.version = 1
        if commit:
            page.save()
        return page
