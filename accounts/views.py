from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, UpdateView
from .models import Account


class AccountUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'accounts/detail.html'
    model = Account


class AccountDetailView(LoginRequiredMixin, DetailView):
    template_name = 'accounts/detail.html'
    model = Account
