from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.views.generic import CreateView, RedirectView
from accounts.models import Account
from .forms import SignInForm, SignUpForm

class SignInView(LoginView):
    template_name = 'authentication/signin.html'
    form_class = SignInForm

class SignUpView(CreateView):
    template_name = 'authentication/signup.html'
    model = Account
    fields = ['username','first_name','last_name']

class SignOutView(LoginRequiredMixin, RedirectView):
    pass
