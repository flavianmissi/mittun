from django.test import TestCase
from django.contrib import admin

from events.models import Location
from events.admin import LocationAdmin


class AdminTestCase(TestCase):

    def test_should_register_location_model(self):
        self.assertIn(Location, admin.site._registry)

    def test_should_register_location_model_with_LocationAdmin_class(self):
        self.assertIsInstance(admin.site._registry[Location], LocationAdmin)
