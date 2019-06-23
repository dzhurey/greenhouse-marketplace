from django.db import models
from django.core.validators import RegexValidator
from tagging.registry import register
from libs.helpers import UserModelHelper

class Vendor(UserModelHelper):
    picture = models.ImageField(upload_to='', blank=True, null=True)
    number_of_employee = models.IntegerField(blank=True, default=0)

    def tag_names(self):
        return ' '.join([tag.name for tag in self.tags])

register(Vendor)