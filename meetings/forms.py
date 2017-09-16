from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from .models import Meeting

class MeetingForm(ModelForm):

    class Meta:
        model = Meeting
        fields = [
            'title',
            'date',
        ]
