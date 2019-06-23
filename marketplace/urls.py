"""marketplace URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users.views import CustomerRegistrationView, VendorRegistrationView, SessionView
from customers.views import DashboardView as CustomerDashboardView
from vendors.views import DashboardView as VendorDashboardView, ProfileView as VendorProfileView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registrations/customers/', CustomerRegistrationView.as_view(), name='customer_registration'),
    path('registrations/vendors/', VendorRegistrationView.as_view(), name='vendor_registration'),
    path('sessions/', SessionView.as_view(), name='session'),
    path('customers/dashboards/', CustomerDashboardView.as_view(), name='customer_dashboard'),
    path('vendors/dashboards/', VendorDashboardView.as_view(), name='vendor_dashboard'),
    path('vendors/profiles/', VendorProfileView.as_view(), name='vendor_profile'),
]
