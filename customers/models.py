from django.db import models
from libs.helpers import UserModelHelper

class Customer(UserModelHelper):
    picture = models.ImageField(upload_to='', blank=True, null=True)
