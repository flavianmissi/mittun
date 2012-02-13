# -*- coding: utf-8 -*-

from datetime import date

from django.test import TestCase
from django.test.client import RequestFactory

from mittun.views import IndexView
from events.models import Event


class IndexViewTestCase(TestCase):

    def setUp(self):
        self.request = RequestFactory().get('index')
        self.event = Event.objects.create(
            name= 'Dojo',
            description= 'Dojo',
            date= date.today(),
        )

    def tearDown(self):
        self.event.delete()

    def test_should_get_the_index_and_get_a_200_status_code(self):
        response = IndexView.as_view()(self.request)
        self.assertEqual(response.status_code, 200)

    def test_index_view_should_use_index_template(self):
        response = IndexView.as_view()(self.request)
        self.assertTrue('index.html' in response.template_name)
