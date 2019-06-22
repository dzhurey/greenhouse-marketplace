from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from users.forms import SessionForm
from customers.models import Customer
from vendors.models import Vendor

class SessionView(View):
    form_class = SessionForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, 'users/sessions/new.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            user, user_type = self.authenticate_user(request, form.get_credentials())
        if user is not None:
            return redirect("{}_dashboard".format(user_type))

        return render(request, 'users/sessions/new.html', {'form': form})

    def delete(self, request, *args, **kwargs):
        logout(request)
        return HttpResponse(302)

    def authenticate_user(self, request, credentials):
        user = authenticate(username=credentials['email'], password=credentials['password'])
        user_object = None
        user_type = ''

        if user is not None:
            user_object = Customer.objects.filter(user=user).first()
            user_type = 'customer'
            if user_object is None:
                user_object = Vendor.objects.filter(user=user).first()
                user_type = 'vendor'
            if user_object:
                login(request, user)

        return user, user_type
