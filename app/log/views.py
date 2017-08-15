# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json

from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from app.log.models import MinuteLog, HourLog
from app.machine.models import Machine


class LogView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(LogView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        obj = get_object_or_404(Machine, code=kwargs['pk'])
        req = request.POST.get('req', None)
        if req:
            try:
                data = json.loads(req)
            except Exception as e:
                print e
                raise Http404()

            if 'hashrate' not in data:
                raise Http404('Hashrate not found')

            log = MinuteLog(machine=obj, rate=int(data['hashrate']))
            log.save()

            try:
                item = HourLog.objects.filter(machine=obj)
                item.send = True
                item.save()
                return JsonResponse({'req': {"gpuid": "reboot"}})
            except ObjectDoesNotExist:
                return HttpResponse(status=304)
        raise Http404("Machine not found")
