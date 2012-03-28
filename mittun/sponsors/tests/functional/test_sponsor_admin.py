from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from mittun.sponsors.models import Sponsor, Category


class SponsorAdminTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser('siminino', 'siminino@simi.com', 'simipass')
        self.category = Category.objects.create(name="categorytest")
        self.sponsor = Sponsor.objects.create(name="nametest",
                               description="desctest",
                               url="http://urlteste.com",
                               category=self.category,
                               user=self.user)
        self.sponsor_without_user = Sponsor.objects.create(name="nametest2",
                                                           description="desctest2",
                                                           url="http://urlteste2.com",
                                                           category=self.category)
        self.client = Client()
        self.client.login(username='siminino', password='simipass')
        self.response = self.client.get('/admin/sponsors/sponsor/')

    def tearDown(self):
        self.sponsor.delete()
        self.user.delete()
        self.category.delete()

    def test_should_request_and_be_success(self):
        self.assertEqual(200, self.response.status_code)

    def test_should_contains_sponsor_on_context(self):
        self.assertIn(self.sponsor, self.response.context['cl'].result_list)

    def test_should_not_has_sponsor_without_user_on_contains(self):
        self.assertNotIn(self.sponsor_without_user, self.response.context['cl'].result_list)
