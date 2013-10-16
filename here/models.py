from django.db import models
from django.contrib.auth.models import User


class Checkin(models.Model):
    event = models.ForeignKey('schedule.Event')
    time_stamp = models.DateTimeField('check in time')
    email = models.EmailField(max_length=254)
    user = models.ForeignKey(User, null=True)
