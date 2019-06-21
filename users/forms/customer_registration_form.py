import re
from django import forms
from django.contrib.auth.models import User
from customers.models import Customer

class CustomerRegistrationForm(forms.Form):
    name = forms.CharField(label='Name', max_length=255, required=True)
    phone = forms.CharField(label='Phone Number', max_length=15, required=True)
    email = forms.EmailField(label='Email', required=True)
    password = forms.CharField(widget=forms.PasswordInput, label='Password', required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput, label='Confirm Password', required=True)

    def save(self, commit=True):
        user = User()
        user.username = self.cleaned_data['email']
        user.email = self.cleaned_data['email']
        user.set_password(self.cleaned_data['password'])

        if commit:
            user.save()

        if user:
            customer_meta = {
                'user': user,
                'name': self.cleaned_data['name'],
                'phone': self.cleaned_data['phone']
            }

            Customer.objects.create(**customer_meta)

        return user

    def clean_confirm_password(self):
        confirm_password = self.cleaned_data['confirm_password']
        password = self.cleaned_data['password']
        if password != confirm_password:
            raise forms.ValidationError("Confirm password must match with your password")

        return confirm_password

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        pattern = re.compile('^\+?1?\d{8,15}$')
        if not pattern.match(phone):
            raise forms.ValidationError("Phone number must be numeric")

        return phone
