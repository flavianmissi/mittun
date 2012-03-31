from mittun.tests.utils import ModelTestCase
from mittun.sponsors.models import Responsibility


class ResponsabilityModelTestCase(ModelTestCase):

    def setUp(self):
        self.responsability = Responsibility.objects.create(description='test')

    def tearDown(self):
        self.responsability.delete()

    def test_should_have_a_description(self):
        self.assertIsFieldPresent('description', Responsibility)
