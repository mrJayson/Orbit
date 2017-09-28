from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from .forms import MeetingForm
from .models import Meeting


class MeetingCreateView(LoginRequiredMixin, CreateView):
    template_name = 'meetings/form.html'
    model = Meeting
    form_class = MeetingForm

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()

        if (self.request.method == 'POST'):
            # pass in the author here
            form = form_class(self.request.user, self.request.POST)
        else:
            form = form_class()
        return form

    def get_success_url(self, **kwargs):
        return reverse('meetings:detail', kwargs={'slug': self.object.slug})


class MeetingDetailView(LoginRequiredMixin, DetailView):
    template_name = 'meetings/detail.html'
    model = Meeting


class MeetingIndexView(LoginRequiredMixin, ListView):
    template_name = 'meetings/index.html'
    model = Meeting


class MeetingEditView(LoginRequiredMixin, UpdateView):
    template_name = 'meetings/form.html'
    model = Meeting
    form_class = MeetingForm

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()

        if (self.request.method == 'POST'):
            # pass in the author here
            form = form_class(self.request.user, self.request.POST)
        else:
            form = form_class()
        return form

    def get_success_url(self, **kwargs):
        return reverse('meetings:detail', kwargs={'slug': self.object.slug})
