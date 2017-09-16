from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from .forms import MeetingForm
from .models import Meeting

class MeetingIndexView(LoginRequiredMixin, ListView):
    template_name = 'meetings/index.html'
    model = Meeting

class MeetingCreateView(LoginRequiredMixin, CreateView):
    template_name = 'meetings/meeting_form.html'
    model = Meeting
    form_class = MeetingForm
