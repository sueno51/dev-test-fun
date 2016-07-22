

from __future__ import unicode_literals

import datetime

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from django.utils import timezone

# Create your models here.
class PinLocation(models.Model):
    pinlocation_text = models.CharField(max_length=200)
    active_since_date = models.DateTimeField('activated date')

    def __str__(self):
        return self.pinlocation_text
    def was_activated_recently(self):
        return self.active_since_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    pinloc = models.ForeignKey(PinLocation,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

