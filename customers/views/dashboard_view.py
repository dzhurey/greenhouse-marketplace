from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from libs.decorators.user_decorators import is_customer

class DashboardView(View):
    @method_decorator(is_customer)
    def get(self, request, *args, **kwargs):
        return render(request, 'customers/dashboards/index.html')
