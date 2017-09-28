from django import forms
from django.utils.translation import ugettext_lazy as _
from pages.forms import PageForm
from .models import Meeting


class MeetingForm(PageForm):

    class Meta(PageForm.Meta):
        model = Meeting
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
