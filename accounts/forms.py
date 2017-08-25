from django import forms

class SignInForm(forms.Form):
    username = forms.CharField();
    password1 = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if (username and password):
            user = authenticate(identification=username, password=password)
            if user is None:
                raise forms.ValidationError(_("Username or password is incorrect, please try again. Note that both fields are case-sensitive."))
        return self.cleaned_data
