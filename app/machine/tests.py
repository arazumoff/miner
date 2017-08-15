# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from app.machine.models import Machine


class MachineTest(TestCase):

    def setUp(self):
        Machine.objects.create(code="1234-9911-0998-2uw2", count="2")
        Machine.objects.create(code="1234-9911-0998-2uw4", count="4")

    def test_machine_count(self):
        count = Machine.objects.all().count()
        self.assertEqual(count, 2)

    def test_return_obj(self):
        obj = Machine.objects.get(code="1234-9911-0998-2uw4")
        self.assertEqual(obj.count, 4)
