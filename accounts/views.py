from django.shortcuts import render
from django.views.generic import CreateView, DetailView, FormView, RedirectView, UpdateView
from .models import Account
from .forms import SignInForm

class SignInView(FormView):
    template_name = 'accounts/sign_in.html'
    form_class = SignInForm
    success_url = '/'

class SignUpView(CreateView):
    model = Account
    fields = ['username','first_name','last_name']

class SignOutView(RedirectView):
    pass

class AccountEditView(UpdateView):
    pass

class AccountDetailView(DetailView):
    pass
