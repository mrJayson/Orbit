from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, UpdateView


class AccountUpdateView(LoginRequiredMixin, UpdateView):
    pass


class AccountDetailView(LoginRequiredMixin, DetailView):
    pass
