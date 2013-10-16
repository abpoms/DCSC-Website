from django.db import models
from django.contrib.auth.models import User


class Committee(models.Model):
    chair = models.ForeignKey(
        User,
        related_name='committee_chair_set',
        verbose_name='committee chair')
    vice_chair = models.ForeignKey(
        User,
        related_name='committee_vice_chair_set',
        verbose_name='vice chair')
    members = models.ManyToManyField(
        User,
        through='Membership',
        verbose_name='members list')
    events = models.ManyToManyField('schedule.Event')


class Membership(models.Model):
    person = models.ForeignKey(User)
    committee = models.ForeignKey(Committee)
    date_joined = models.DateField()
