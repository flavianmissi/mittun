from django.test import TestCase


class ModelTestCase(TestCase):

    def assertIsFieldPresent(self, field, model):
        self.assertIn(field, model._meta.get_all_field_names())
