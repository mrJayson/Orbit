from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from accounts.models import Account


class SignInForm(AuthenticationForm):

    username = forms.CharField(
        required=True,
        label="",
        max_length=32,
        widget=forms.TextInput(attrs={
            'placeholder': 'Username',
            'class': 'form-control',
        }),
    )
    password = forms.CharField(
        required=True,
        label="",
        max_length=32,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',
            'class': 'form-control',
        }),
    )


class SignUpForm(ModelForm):

    error_messages = {
        'password_mismatch': _("The two password fields do not match")
    }

    class Meta:
        model = Account
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
            'bio',
        ]

    first_name = forms.CharField(
        required=True,
        label="",
        max_length=32,
        widget=forms.TextInput(attrs={
            'placeholder': 'First Name',
            'class': 'form-control',
        }),
    )
    last_name = forms.CharField(
        required=True,
        label="",
        max_length=32,
        widget=forms.TextInput(attrs={
            'placeholder': 'Last Name',
            'class': 'form-control',
        }),
    )
    username = forms.CharField(
        required=True,
        label="",
        max_length=32,
        widget=forms.TextInput(attrs={
            'placeholder': 'Username',
            'class': 'form-control',
        }),
    )
    email = forms.CharField(
        required=False,
        label="",
        max_length=32,
        widget=forms.EmailInput(attrs={
            'placeholder': 'Email',
            'class': 'form-control',
        }),
    )
    password1 = forms.CharField(
        required=True,
        label="",
        max_length=32,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',
            'class': 'form-control',
        }),
    )
    password2 = forms.CharField(
        required=True,
        label="",
        max_length=32,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Confirm Password',
            'class': 'form-control',
        }),
    )
    bio = forms.CharField(
        required=False,
        label="",
        widget=forms.Textarea(attrs={
            'placeholder': 'Tell us a bit about yourself',
            'class': 'form-control',
        }),
    )

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if (password1 and password2 and password1 != password2):
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        self.instance.username = self.cleaned_data.get('username')
        password_validation.validate_password(
            self.cleaned_data.get('password2'), self.instance)
        return password2

    def save(self, commit=True):
        account = super(SignUpForm, self).save(commit=False)
        account.set_password(self.cleaned_data["password1"])
        if commit:
            account.save()
        return account
