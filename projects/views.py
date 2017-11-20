from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import ListView, DetailView
from pages.views import PageCreateView, PageDetailView, PageUpdateView
from .forms import ProjectForm
from .models import Project, Task


class ProjectBoardView(LoginRequiredMixin, DetailView):
    template_name = 'projects/board.html'
    model = Project

    def get_context_data(self, *args, **kwargs):
        context = super(ProjectBoardView, self).get_context_data(*args, **kwargs)
        context['to_do'] = Task.objects.filter(project=self.object, column=Project.to_do)
        context['in_progress'] = Task.objects.filter(project=self.object, column=Project.in_progress)
        context['completed'] = Task.objects.filter(project=self.object, column=Project.completed)
        return context


class ProjectCreateView(PageCreateView):
    template_name = 'projects/form.html'
    model = Project
    form_class = ProjectForm

    def get_success_url(self, **kwargs):
        return reverse('projects:detail', kwargs={'slug': self.object.slug})


class ProjectDetailView(PageDetailView):
    template_name = 'projects/detail.html'
    model = Project


class ProjectIndexView(LoginRequiredMixin, ListView):
    template_name = 'projects/index.html'
    model = Project
    queryset = Project.objects.filter(is_removed=False)


class ProjectUpdateView(PageUpdateView):
    template_name = 'projects/form.html'
    model = Project
    form_class = ProjectForm
