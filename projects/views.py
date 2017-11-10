from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import ListView
from pages.views import PageCreateView, PageDetailView
from .forms import ProjectForm
from .models import Project


class ProjectIndexView(LoginRequiredMixin, ListView):
    template_name = 'projects/index.html'
    model = Project


class ProjectDetailView(PageDetailView):
    template_name = 'projects/detail.html'
    model = Project


class ProjectCreateView(PageCreateView):
    template_name = 'projects/form.html'
    model = Project
    form_class = ProjectForm

    def get_success_url(self, **kwargs):
        return reverse('projects:detail', kwargs={'slug': self.object.slug})
