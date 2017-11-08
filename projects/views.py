from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import Project


class ProjectIndexView(LoginRequiredMixin, ListView):
    template_name = 'projects/index.html'
    model = Project
