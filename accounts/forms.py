from django import forms
from .models import Account


class AccountAdminForm(forms.ModelForm):
    class Meta:
        model = Account
        exclude = (
            'date_joined',
            'groups',
            'last_login',
            'password',
            'superuser_status',
            'user_permissions',
        )
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'bio',
            'is_staff',
            'is_active',
        )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        return email.lower()

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        return first_name.capitalize()

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        return last_name.capitalize()

    def clean_username(self):
        username = self.cleaned_data.get('username')
        return username.lower()
