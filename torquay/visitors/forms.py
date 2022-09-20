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


class BookingForm(forms.ModelForm):
    room = forms.ModelChoiceField(queryset=Category.objects.all(),
                                    to_field_name = 'name',
                                    empty_label="Select a Room Type",
                                    label='Room Type')

    number_of_people = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'class':'form-control',
            'type': 'number',
            'max': '5',
            'placeholder':'0',
            'min':'0'
        }
               
    )
    )

    class Meta:
        model = Booking
        fields = ['room','check_in_date', 'check_out_date','number_of_people']
        widgets = {
            'check_in_date' : forms.DateInput(
                format=('%m-%d-%Y'),
                attrs= {
                    'class':'form-control', 
                    'placeholder':'Select a date', 
                    'type':'date'
                }
            ),

            'check_out_date' : forms.DateInput(
                format=('%m-%d-%Y'),
                attrs= {
                    'class':'form-control', 
                    'placeholder':'Select a date', 
                    'type':'date'
                }
            ),

        }