from sponsors.tests.unit.utils import ModelTestCase
from sponsors.models import Category


class CategoryModelTestCase(ModelTestCase):

    def test_should_have_a_name(self):
        self.assertIsFieldPresent('name', Category)
