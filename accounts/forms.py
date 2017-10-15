from django import forms
from .models import Account


class AccountAdminForm(forms.ModelForm):
    class Meta:
        model = Account
        exclude = ()
        widgets = {
            'password': forms.PasswordInput(),
        }

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(AccountAdminForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
