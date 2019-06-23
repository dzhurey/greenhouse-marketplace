from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib import messages
from tagging.models import Tag
from libs.decorators.user_decorators import is_vendor
from vendors.forms import ProfileForm
from vendors.models import Vendor

class ProfileView(View):
    form_class = ProfileForm

    @method_decorator(is_vendor)
    def get(self, request, *args, **kwargs):
        vendor = Vendor.objects.get(user=request.user)
        form = self.form_class(instance=vendor, initial={'vendor_categories': ' '.join([tag.name for tag in vendor.tags])})
        return render(request, 'vendors/profiles/edit.html', {'form': form})

    @method_decorator(is_vendor)
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            try:
                instance = form.save(commit=False)
                instance.user = request.user
                instance.id = Vendor.objects.get(user=request.user).id
                instance.save()
                Tag.objects.update_tags(instance, form.cleaned_data['vendor_categories'])
            except Exception as identifier:
                messages.error(request, identifier)

        return render(request, 'vendors/profiles/edit.html', {'form': form})