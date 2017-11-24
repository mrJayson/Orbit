from django import forms
from django.utils.translation import ugettext_lazy as _
from pages.forms import PageForm
from .models import Project, Task
from django.db.models import Max


class ProjectForm(PageForm):

    class Meta:
        model = Project
        fields = [
            'title',
            'code',
            'content',
            'changelog',
        ]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _("Title goes here..."),
            }),
            'code': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _("Project Code"),
            }),
            'changelog': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _("What did you change?"),
            }),
        }


class TaskForm(PageForm):

    def __init__(self, *args, **kwargs):
        self.project = kwargs.pop('project', None)
        super(TaskForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Task
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

    def save(self, commit=True):
        task = super(TaskForm, self).save(commit=False)
        task.task_project = self.project
        code = Task.objects.filter(task_project=self.project).aggregate(Max('code')).get('code__max')
        if code is None:
            code = 1
        else:
            code += 1
        task.code = code
        if commit:
            task.save()
        return task
