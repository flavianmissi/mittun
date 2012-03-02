from mittun.tests.utils import ModelTestCase
from mittun.events.models import Location


class LocationModelTestCase(ModelTestCase):

    def test_should_have_a_title(self):
        self.assertIsFieldPresent('title', Location)

    def test_should_have_an_event(self):
        self.assertIsFieldPresent('event', Location)

    def test_should_have_an_address(self):
        self.assertIsFieldPresent('address', Location)
