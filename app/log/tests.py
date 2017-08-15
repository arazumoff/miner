# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.test import Client
from django.test import TestCase


class LogTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_validation_get_method(self):
        response = self.client.get('/log/machine/123/')
        self.assertEqual(response.status_code, 405)

    def test_novalid_json(self):
        response = self.client.post('/log/machine/123/', {
            'req': '{"hashrate": 782, "vcards": [[{"gpuid": 1}, {"gpuid": 2}]}'
        })
        self.assertEqual(response.status_code, 404)

    def test_validation_uid(self):
        response = self.client.post('/log/machine/123/', {
            'req': json.dumps({
                "hashrate": 782,
                "vcards": [{"gpuid": 1}, {"gpuid": 2}]
            })})
        self.assertEqual(response.status_code, 404)
