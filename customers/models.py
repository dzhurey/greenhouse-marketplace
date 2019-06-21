from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

class Customer(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{8,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15, validators=[phone_regex])
    picture = models.ImageField(upload_to='', blank=True, null=True)

    def __str__(self):
        return self.name
