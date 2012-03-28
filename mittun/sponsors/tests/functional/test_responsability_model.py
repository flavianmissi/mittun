from mittun.tests.utils import ModelTestCase
from mittun.sponsors.models import Responsibility


class ResponsabilityModelTestCase(ModelTestCase):

    def setUp(self):
        self.responsibility = Responsibility.objects.create(description='test')

    def tearDown(self):
        self.responsibility.delete()

    def test_should_have_a_description(self):
        self.assertIsFieldPresent('description', Responsibility)

    def test_should_return_resposibility_description_when_called_by_unicode(self):
        self.assertEqual("test", unicode(self.responsibility))
