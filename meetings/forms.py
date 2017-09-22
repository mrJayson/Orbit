from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from .models import Meeting

class MeetingForm(ModelForm):

    class Meta:
        model = Meeting
        fields = [
            'title',
            'start',
            'end',
            'content',
        ]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title',
            }),
            'start': forms.DateInput(attrs={
                'class': 'form-control',
                'placeholder':'Start',
            }),
            'end': forms.DateInput(attrs={
                'class': 'form-control',
                'placeholder':'End',
            }),
        }
