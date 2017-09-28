from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from accounts.models import Account
from orbit.settings import ACCOUNTS_DISABLE_SIGNUP
from .forms import SignInForm, SignUpForm


class SignInView(LoginView):
    template_name = 'authentication/signin.html'
    form_class = SignInForm

    def get_context_data(self, *args, **kwargs):
        context = super(SignInView, self).get_context_data(*args, **kwargs)
        context['ACCOUNTS_DISABLE_SIGNUP'] = ACCOUNTS_DISABLE_SIGNUP
        return context


class SignOutView(LoginRequiredMixin, LogoutView):
    next_page = reverse_lazy('dashboard:dashboard')


class SignUpView(SuccessMessageMixin, UserPassesTestMixin, CreateView):
    model = Account
    form_class = SignUpForm
    template_name = 'authentication/signup.html'
    success_url = reverse_lazy('authentication:signin')
    success_message = _("You have successfully signed up! Please sign in with your credentials")
    signup_disabled_message = _("Account signups are disabled, please contact an Outburst Administrator for assistance")

    # Do not allow access to view if signups are disabled
    def test_func(self):
        if (ACCOUNTS_DISABLE_SIGNUP):
            messages.error(self.request, self.signup_disabled_message)
        return not(ACCOUNTS_DISABLE_SIGNUP)

    # For this use case, redirect is redundant
    def get_redirect_field_name(self):
        return ''
