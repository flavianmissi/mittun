from mittun.tests.utils import ModelTestCase
from mittun.sponsors.models import Bonus


class BonusModelTestCase(ModelTestCase):

    def setUp(self):
        self.bonus = Bonus.objects.create(description='test')

    def tearDown(self):
        self.bonus.delete()

    def test_should_have_a_description(self):
        self.assertIsFieldPresent('description', Bonus)

