from django.test import TestCase

from events.forms import BootstrapForm
from events.models import Event


class BootstrapFormTestCase(TestCase):

    def setUp(self):
        self.form = BootstrapForm()

    def test_should_have_a_model(self):
        self.assertEqual(Event, self.form._meta.model)
