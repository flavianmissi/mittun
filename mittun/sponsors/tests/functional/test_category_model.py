from mittun.tests.utils import ModelTestCase
from sponsors.models import Category


class CategoryModelTestCase(ModelTestCase):

    def setUp(self):
        self.category = Category.objects.create(name='diamond')

    def tearDown(self):
        self.category.delete()

    def test_should_have_a_name(self):
        self.assertIsFieldPresent('name', Category)

    def test_should_return_name_when_called_by_unicode(self):
        self.assertEqual('diamond', unicode(self.category))
