from sponsors.tests.unit.utils import ModelTestCase

from sponsors.models import Sponsor


class SponsorModelTestCase(ModelTestCase):

    def test_model_should_have_a_name_field(self):
        self.assertIsFieldPresent('name', Sponsor)

    def test_model_should_have_a_description(self):
        self.assertIsFieldPresent('description', Sponsor)

    def test_model_should_have_a_logo(self):
        self.assertIsFieldPresent('logo', Sponsor)

    def test_model_should_have_a_url(self):
        self.assertIsFieldPresent('url', Sponsor)

    def test_model_should_have_a_category(self):
        self.assertIsFieldPresent('category', Sponsor)
