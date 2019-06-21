import re
from django import forms
from django.contrib.auth.models import User
from customers.models import Customer

class SessionForm(forms.Form):
    email = forms.EmailField(label='Email', required=True)
    password = forms.CharField(widget=forms.PasswordInput, label='Password', required=True)

    def get_credentials(self):
        return {
            'email': self.cleaned_data['email'],
            'password': self.cleaned_data['password']
        }
