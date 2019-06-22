from django import forms
from users.forms.user_registration_form import UserRegistrationForm
from customers.models import Customer

class CustomerRegistrationForm(UserRegistrationForm):
    user_model = Customer
