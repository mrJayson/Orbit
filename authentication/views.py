from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from accounts.models import Account
from .forms import SignInForm, SignUpForm

class SignInView(LoginView):
    template_name = 'authentication/signin.html'
    form_class = SignInForm

class SignUpView(SuccessMessageMixin, CreateView):
    model = Account
    form_class = SignUpForm
    template_name = 'authentication/signup.html'
    success_url = reverse_lazy('authentication:signin')
    success_message = _("You have successfully signed up! Please sign in with your credentials")

class SignOutView(LoginRequiredMixin, LogoutView):
    next_page = reverse_lazy('dashboard:dashboard')
