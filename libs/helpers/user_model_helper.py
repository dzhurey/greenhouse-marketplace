from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

class UserModelHelper(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name
