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
        import pdb; pdb.set_trace();
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
