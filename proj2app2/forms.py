from django import forms
from .models import CbvContactinfo
from django.forms import ModelForm, TextInput, EmailInput, Textarea, PasswordInput 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation 

class CbvContactForm(forms.ModelForm):
    class Meta:
        model = CbvContactinfo
        fields = ['cbvname', 'cbvemail', 'cbvmessage'] 

        labels = {
            'cbvname': 'Name*',
            'cbvemail': 'Email*',
            'cbvmessage': 'Message*',
        }

        widgets = {
            'cbvname': TextInput(attrs={
                'class': "form-control w-50",
                'style': 'margin-top:5px',
                'placeholder': 'Your Name'
                }),
            'cbvemail': EmailInput(attrs={
                'class': "form-control w-50 mt-2",
                #'style': 'max-width: 300px;',
                'placeholder': 'Your Email'
                }),
            'cbvmessage': Textarea(attrs={
                'class': "form-control w-50 mt-2",
                #'style': 'height: 150px;',
                'placeholder': 'Your messgae...',
                'rows':"5"
                })
        }

#signup2 form
class SignUpViewform2(UserCreationForm):
         
    email = forms.EmailField(
        label=("Email"),
        max_length=254, 
        widget=forms.EmailInput(attrs={"autocomplete": "email", "class": "form-control w-50", "placeholder":"Email"}),
        help_text='Required. Inform a valid email address.',
    )
          
     
    password1 = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "class": "form-control w-50", "placeholder":"Password"}),
        help_text=password_validation.password_validators_help_text_html(),
    )

    password2 = forms.CharField(
        label=("Confirme Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "class": "form-control w-50", "placeholder":"Confirm password"}),
        help_text=("Re-Enter the same password."),
      
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        widgets = {
            'username': TextInput(attrs={
                'class': "form-control w-50",
                'style': 'margin-top:5px',
                'placeholder': 'Username'
                }),
        }


#login2 form
class LoginForm2(AuthenticationForm):
    username = forms.CharField(label='Email / Username')