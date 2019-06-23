from django import forms
from customers.models import Customer

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'phone']
