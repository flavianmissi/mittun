from mittun.tests.utils import ModelTestCase
from mittun.sponsors.models import Requirement


class RequirementModelTestCase(ModelTestCase):

    def setUp(self):
        self.requirement = Requirement.objects.create(description='test')

    def tearDown(self):
        self.requirement.delete()

    def test_should_have_a_description(self):
        self.assertIsFieldPresent('description', Requirement)

    def test_should_return_requirement_description_when_called_by_unicode(self):
        self.assertEqual("test", unicode(self.requirement))
