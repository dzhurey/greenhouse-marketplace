from django import forms
from vendors.models import Vendor

class ProfileForm(forms.ModelForm):
    vendor_categories = forms.CharField(label='Vendor Categories', required=False)

    class Meta:
        model = Vendor
        fields = ['name', 'phone', 'number_of_employee']
