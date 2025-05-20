from .models import AccountInfo 
from django import forms
from django.contrib.auth.hashers import make_password


class AccountInfoForm(forms.ModelForm):
    confirmation = forms.CharField(
        max_length=140,
        widget=forms.PasswordInput(),
        label='Confirm your password'
    )
    # The field above masks the password input with dots while typing.

    class Meta:
        model = AccountInfo
        fields = ('name', 'email', 'password', 'confirmation', 'gender', 'birthdate', 'phone')
        widgets = {
            'password': forms.PasswordInput()
        }
        error_messages = {
            'name': {
                'required': 'Please enter a username.'
            },
            'email': {
                'required': 'Please enter an email address.',
                'unique': 'This email is already registered. Try another.'
            },
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirmation = cleaned_data.get('confirmation')

        if password and confirmation and password != confirmation:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get('password')
        if password:
            user.password = make_password(password)
        if commit:
            user.save()
        return user
