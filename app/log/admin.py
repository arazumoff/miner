# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import HourLog


@admin.register(HourLog)
class LogAdmin(admin.ModelAdmin):
    pass
