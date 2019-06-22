from django.contrib.auth.decorators import user_passes_test
from vendors.models import Vendor
from customers.models import Customer

def check_vendor(user):
    if user.is_authenticated:
        return Vendor.objects.filter(user=user).exists()

    return False


def is_vendor(fn=None):
    decorator = user_passes_test(check_vendor, login_url='session')

    if fn:
        return decorator(fn)

    return decorator

def check_customer(user):
    if user.is_authenticated:
        return Customer.objects.filter(user=user).exists()

    return False


def is_customer(fn=None):
    decorator = user_passes_test(check_customer, login_url='session')

    if fn:
        return decorator(fn)

    return decorator
