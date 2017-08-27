from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import DetailView, UpdateView
from django.urls import reverse_lazy

class AccountEditView(LoginRequiredMixin, UpdateView):
    pass

class AccountDetailView(LoginRequiredMixin, DetailView):
    pass
