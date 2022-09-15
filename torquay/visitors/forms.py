from django import forms
from .models import * 
from django.contrib.auth.models import User

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password']
        widgets = {
            'username' : forms.TextInput(
                attrs= {
                    'class':'form-control '
                }
            ),
            'first_name' : forms.TextInput(
                attrs= {
                    'class':'form-control '
                }
            ),
            'last_name' : forms.TextInput(
                attrs= {
                    'class':'form-control '
                }
            ),
            'email' : forms.EmailInput(
                attrs= {
                    'class':'form-control '
                }
            ),
            'password' : forms.PasswordInput(
                attrs= {
                    'class':'form-control '
                }
            )
        }

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password']
        widgets = {
            'username' : forms.TextInput(
                attrs= {
                    'class':'form-control'
                }
            ),
            'password' : forms.PasswordInput(
                attrs= {
                    'class':'form-control'
                }
            )
        }
