from django import forms
from django.utils.translation import ugettext_lazy as _
from pages.forms import PageForm
from .models import Event


class EventForm(PageForm):

    class Meta(PageForm.Meta):
        model = Event
        fields = PageForm.Meta.fields + ['start', 'end']
        widgets = PageForm.Meta.widgets.copy()
        widgets.update({
            'start': forms.DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Start',
            }),
            'end': forms.DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'End',
            }),
        })
