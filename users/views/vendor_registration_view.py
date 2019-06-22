from django.shortcuts import render
from django.views import View
from django.db import IntegrityError
from django.contrib import messages
from users.forms import VendorRegistrationForm

class VendorRegistrationView(View):
    form_class = VendorRegistrationForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, 'users/registrations/vendor.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            try:
                form.save()
            except IntegrityError:
                messages.error(request, "Email that you're entered is already used")

        return render(request, 'users/registrations/vendor.html', {'form': form})
