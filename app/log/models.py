# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

from app.machine.models import Machine


class MinuteLog(models.Model):
    machine = models.ForeignKey(Machine, related_name="minuts")
    rate = models.IntegerField()
    sync = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


class HourLog(models.Model):
    machine = models.ForeignKey(Machine, related_name="hours")
    rate = models.IntegerField('Avg rate per hour')
    send = models.BooleanField('Send command', default=False)
    created_at = models.DateTimeField(auto_now_add=True)
