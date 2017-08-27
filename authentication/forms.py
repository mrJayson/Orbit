from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

class SignInForm(AuthenticationForm):
    username = forms.CharField(
        required = True,
        label = "",
        max_length = 32,
        widget=forms.TextInput(attrs={'placeholder': 'Username'}),
    )
    password = forms.CharField(
        required = True,
        label = "",
        max_length = 32,
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
    )

class SignUpForm(forms.Form):
    first_name = forms.CharField(
        required = True,
        label = "",
        max_length = 32,
        widget=forms.TextInput(attrs={'placeholder': 'First Name'}),
    )
    last_name = forms.CharField(
        required = True,
        label = "",
        max_length = 32,
        widget=forms.TextInput(attrs={'placeholder': 'Last Name'}),
    )
    username = forms.CharField(
        required = True,
        label = "",
        max_length = 32,
        widget=forms.TextInput(attrs={'placeholder': 'Username'}),
    )
    email = forms.CharField(
        required = False,
        label = "",
        max_length = 32,
        widget=forms.TextInput(attrs={'placeholder': 'Email'}),
    )
    password = forms.CharField(
        required = True,
        label = "",
        max_length = 32,
        widget = forms.PasswordInput(attrs={'placeholder': 'Password'}),
    )
    confirm_password = forms.CharField(
        required = True,
        label = "",
        max_length = 32,
        widget = forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}),
    )
    bio = forms.CharField(
        required = False,
        widget = forms.TextInput(attrs={'placeholder': 'Tell us a bit about yourself'}),
    )
