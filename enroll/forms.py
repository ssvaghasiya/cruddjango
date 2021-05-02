from django.core import validators
from django import forms
from .models import User


class StudentRegistration(forms.ModelForm):

    class Meta:
        model = User
        fields = ['name', 'email', 'password']
        # labels = {'name': 'Enter Name', 'email': 'Enter Email',
        #           'password': 'Enter Password'}
        # error_messages = {
        #     'name': {'required': 'Name Field is empty'},
        #     'password': {'required': 'password Field is empty'},
        #     'email': {'required': 'Email Field is empty'}
        # }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Plz Enter Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Plz Enter Your Email'}),
            'password': forms.PasswordInput(render_value=True,  attrs={'class': 'form-control', 'placeholder': 'Plz Enter Your Password'}),

        }

