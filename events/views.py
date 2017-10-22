from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import ListView
from .forms import EventForm
from .models import Event
from pages.views import PageCreateView, PageDetailView, PageHistoryView, PageUpdateView


class EventCreateView(PageCreateView):
    template_name = 'events/form.html'
    model = Event
    form_class = EventForm

    def get_success_url(self, **kwargs):
        return reverse('events:detail', kwargs={'slug': self.object.slug})


class EventDetailView(PageDetailView):
    template_name = 'events/detail.html'
    model = Event


class EventHistoryView(PageHistoryView):
    model = Event


class EventIndexView(LoginRequiredMixin, ListView):
    template_name = 'events/index.html'
    model = Event
    queryset = Event.objects.filter(is_removed=False)
    ordering = ['-creation_date']


class EventUpdateView(PageUpdateView):
    template_name = 'events/form.html'
    model = Event
    form_class = EventForm

    def get_success_url(self, **kwargs):
        return reverse('events:detail', kwargs={'slug': self.object.slug})
