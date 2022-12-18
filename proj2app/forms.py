from django import forms
from django.forms import TextInput, EmailInput,PasswordInput


class UserRegistrationForm(forms.Form):
    username = forms.CharField(
        required = True,
        label = 'Username',
        max_length = 32,
        widget = forms.TextInput(attrs={'placeholder': 'Your username'})
    )
    email = forms.CharField(
        required = True,
        label = 'Email',
        max_length = 32,
        widget = forms.EmailInput(attrs={'placeholder': 'Your Email'})
    )
    password = forms.CharField(
        required = True,
        label = 'Password',
        max_length = 32,
        widget = forms.PasswordInput(attrs={'placeholder': 'Password'})
    )