from django.test import TestCase

from sponsors.models import Sponsor


class SponsorModelTestCase(TestCase):

    def test_model_should_have_a_name_field(self):
        self.assertIsFieldPresent('name')

    def test_model_should_have_a_description(self):
        self.assertIsFieldPresent('description')

    def test_model_should_have_a_logo(self):
        self.assertIsFieldPresent('logo')

    def assertIsFieldPresent(self, field):
        self.assertIn(field, Sponsor._meta.get_all_field_names())
