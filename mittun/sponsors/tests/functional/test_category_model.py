from mittun.tests.utils import ModelTestCase
from mittun.sponsors.models import Category


class CategoryModelTestCase(ModelTestCase):

    @classmethod
    def setUpClass(self):
        self.category = Category.objects.create(name_en_us='diamond', name_pt_br='diamante', priority=1)

    @classmethod
    def tearDownClass(self):
        self.category.delete()

    def test_should_have_a_name_for_english(self):
        self.assertIsFieldPresent('name_en_us', Category)

    def test_should_have_a_name_for_portuguese(self):
        self.assertIsFieldPresent('name_pt_br', Category)

    def test_should_return_name_when_called_by_unicode(self):
        self.assertEqual('diamond', unicode(self.category))

    def test_should_have_a_priority_field(self):
        self.assertIsFieldPresent('priority', Category)
