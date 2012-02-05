from django.test import TestCase
from django.contrib import admin
from events.models import Event


class EventAdminTestCase(TestCase):

    def test_should_register_event_model(self):
        self.assertIn(Event, admin.site._registry)
