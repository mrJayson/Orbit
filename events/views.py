from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from .forms import EventForm
from .models import Event


class EventCreateView(LoginRequiredMixin, CreateView):
    template_name = 'events/form.html'
    model = Event
    form_class = EventForm

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
        return reverse('events:detail', kwargs={'slug': self.object.slug})


class EventDetailView(LoginRequiredMixin, DetailView):
    template_name = 'events/detail.html'
    model = Event


class EventIndexView(LoginRequiredMixin, ListView):
    template_name = 'events/index.html'
    model = Event


class EventEditView(LoginRequiredMixin, UpdateView):
    template_name = 'events/form.html'
    model = Event
    form_class = EventForm

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
        return reverse('events:detail', kwargs={'slug': self.object.slug})
