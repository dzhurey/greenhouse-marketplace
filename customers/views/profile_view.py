from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib import messages
from libs.decorators.user_decorators import is_customer
from customers.forms import ProfileForm
from customers.models import Customer

class ProfileView(View):
    form_class = ProfileForm

    @method_decorator(is_customer)
    def get(self, request, *args, **kwargs):
        customer = Customer.objects.get(user=request.user)
        form = self.form_class(instance=customer)
        return render(request, 'customers/profiles/edit.html', {'form': form})

    @method_decorator(is_customer)
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            try:
                instance = form.save(commit=False)
                instance.user = request.user
                instance.id = Customer.objects.get(user=request.user).id
                instance.save()
            except Exception as identifier:
                messages.error(request, identifier)

        return render(request, 'customers/profiles/edit.html', {'form': form})