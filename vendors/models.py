from django.db import models
from django.core.validators import RegexValidator
from libs.helpers import UserModelHelper

class Vendor(UserModelHelper):
    picture = models.ImageField(upload_to='', blank=True, null=True)
