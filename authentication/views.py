from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from accounts.models import Account
from .forms import SignInForm, SignUpForm

class SignInView(LoginView):
    template_name = 'authentication/signin.html'
    form_class = SignInForm

    def get_context_data(self, *args, **kwargs):
        context = super(SignInView, self).get_context_data(*args, **kwargs)

        # A message has been given to display as an alert
        if (self.request.GET.get('alert_message', None)):
            context['alert_message'] = self.request.GET.get('alert')
        return context

class SignUpView(CreateView):
    success_message = _("Thank you for signing up, please sign in.")
    template_name = 'authentication/signup.html'
    model = Account
    form_class = SignUpForm

    # success_url = reverse_lazy('authentication:signin')
    def get_success_url(self):
        return reverse_lazy('authentication:signin')

class SignOutView(LoginRequiredMixin, LogoutView):
    next_page = reverse_lazy('authentication:signin')
