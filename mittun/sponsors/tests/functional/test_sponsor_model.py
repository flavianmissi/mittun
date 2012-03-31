from django.db import models
from django.contrib.auth.models import User, Permission

from mittun.tests.utils import ModelTestCase
from mittun.sponsors.models import Sponsor, Category


class SponsorModelTestCase(ModelTestCase):

    @classmethod
    def setUpClass(self):
        self.category = Category.objects.create(name_en_us='test', priority=1)
        self.user = User.objects.create_user('derp', 'derp@derpmail.com', 'derppass')
        self.sponsor = Sponsor.objects.create(
            name='sponsor name',
            description_en_us='sponsor description',
            url='sponsorurl.com',
            category=self.category,
            user = self.user
        )

    @classmethod
    def tearDownClass(self):
        self.category.delete()
        self.sponsor.delete()

    def test_model_should_have_a_name_field(self):
        self.assertIsFieldPresent('name', Sponsor)

    def test_model_should_have_a_en_us_description(self):
        self.assertIsFieldPresent('description_en_us', Sponsor)

    def test_model_should_have_a_pt_br_description(self):
        self.assertIsFieldPresent('description_pt_br', Sponsor)

    def test_description_should_be_a_text_field(self):
        self.assertIsInstance(self.sponsor._meta._name_map['description_en_us'][0], models.TextField)

    def test_model_should_have_a_logo(self):
        self.assertIsFieldPresent('logo', Sponsor)

    def test_model_should_have_a_url(self):
        self.assertIsFieldPresent('url', Sponsor)

    def test_model_should_have_a_category(self):
        self.assertIsFieldPresent('category', Sponsor)

    def test_should_return_sponsor_name_when_called_by_unicode(self):
        self.assertEqual('sponsor name', unicode(self.sponsor))

    def test_model_should_have_a_user(self):
        self.assertIsFieldPresent('user', Sponsor)

    def test_user_should_be_staff(self):
        user = User.objects.get(id=self.user.id)
        self.assertTrue(user.is_staff)

    def test_user_should_have_sponsor_permissions(self):
        self.assertTrue(self.user.has_perm('sponsors.change_sponsor'))
        self.assertTrue(self.user.has_perm('sponsors.delete_sponsor'))
        self.assertFalse(self.user.has_perm('sponsors.add_sponsor'))

    def test_user_should_have_contact_permissions(self):
        self.assertTrue(self.user.has_perm('sponsors.add_contact'))
        self.assertTrue(self.user.has_perm('sponsors.change_contact'))
        self.assertTrue(self.user.has_perm('sponsors.delete_contact'))

    def test_user_should_have_job_permissions(self):
        self.assertTrue(self.user.has_perm('sponsors.add_job'))
        self.assertTrue(self.user.has_perm('sponsors.change_job'))
        self.assertTrue(self.user.has_perm('sponsors.delete_job'))
