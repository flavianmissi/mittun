from django.test import TestCase
from mittun.sponsors.models import Job, Category, Sponsor


class ModelTestCase(TestCase):

    def assertIsFieldPresent(self, field, model):
        self.assertIn(field, model._meta.get_all_field_names())

    def create_job(self):
        category = Category.objects.create(name='test')
        company = Sponsor.objects.create(name='test', description='test', url='http://test.com', category=category)
        return Job.objects.create(title='test', location='test', description='test', company=company)
