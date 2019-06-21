from django.shortcuts import render
from django.views import View
from users.forms import CustomerRegistrationForm

class CustomerRegistrationView(View):
    form_class = CustomerRegistrationForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, 'users/registrations/customer.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()

        return render(request, 'users/registrations/customer.html', {'form': form})
