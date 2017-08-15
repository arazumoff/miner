# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Machine(models.Model):
    code = models.CharField(u'Уникальный код машины', unique=True, db_index=True, max_length=32)
    count = models.IntegerField(u'Количетсов видеокарт')


class Config(models.Model):
    count = models.IntegerField(u'Количетсов видеокарт', unique=True)
    avg = models.IntegerField(u'Средний показатель',
                              help_text=u'Средний показатель для указанного количества видеокарт')
    variance = models.IntegerField(u'Отклонение %')
