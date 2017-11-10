from django import forms
from django.utils.translation import ugettext_lazy as _
from pages.forms import PageForm
from .models import Project


class ProjectForm(PageForm):

    class Meta:
        model = Project
        fields = [
            'title',
            'content',
            'changelog',
        ]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _("Title goes here..."),
            }),
            'changelog': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _("What did you change?"),
            }),
        }
