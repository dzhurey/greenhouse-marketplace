from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from libs.decorators.user_decorators import is_vendor

class DashboardView(View):
    @method_decorator(is_vendor)
    def get(self, request, *args, **kwargs):
        return render(request, 'vendors/dashboards/index.html')
