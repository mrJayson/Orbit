from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from .models import Page

class PageCreateForm(ModelForm):

    error_messages = {
        'password_mismatch' : _("The two password fields do not match")
    }

    def __init__(self, account=None, *args, **kwargs):
        self.account = account
        super(PageCreateForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Page
        fields = [
            'title',
            'content',
        ]

    title = forms.CharField(
        required = True,
        label = "",
        max_length = 50,
        widget=forms.TextInput(attrs={
            'placeholder' : _("Page Title"),
            'class' : 'form-control',
        }),
    )
    content = forms.CharField(
        required = False,
        label = "",
        widget = forms.Textarea(attrs={
            'placeholder' : _("Begin typing here"),
            'class' : 'form-control',
        }),
    )

    def save(self, commit = True):
        page = super(PageCreateForm, self).save(commit=False)
        page.author = self.account
        page.version = 1
        if commit:
            page.save()
        return page
