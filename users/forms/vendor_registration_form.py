from django import forms
from users.forms.user_registration_form import UserRegistrationForm
from vendors.models import Vendor

class VendorRegistrationForm(UserRegistrationForm):
    user_model = Vendor
