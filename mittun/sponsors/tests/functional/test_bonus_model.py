from mittun.tests.utils import ModelTestCase
from mittun.sponsors.models import Bonus


class BonusModelTestCase(ModelTestCase):

    def setUp(self):
        job = self.create_job()
        self.bonus = Bonus.objects.create(description='test', job=job)

    def tearDown(self):
        self.bonus.delete()

    def test_should_have_a_description(self):
        self.assertIsFieldPresent('description', Bonus)

    def test_should_return_bonus_description_when_called_by_unicode(self):
        self.assertEqual("test", unicode(self.bonus))
