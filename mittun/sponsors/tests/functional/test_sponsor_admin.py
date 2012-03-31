from django.test import TestCase, Client
from django.contrib.auth.models import User, Permission

from mittun.sponsors.models import Sponsor, Category


class SponsorAdminTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user('siminino', 'siminino@simi.com', 'simipass')
        self.user.is_staff = True
        sponsor_permissions = Permission.objects.filter(codename__contains='sponsor')
        self.user.user_permissions.add(*sponsor_permissions)
        self.user.save()

        self.category = Category.objects.create(name="categorytest", priority=1)
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
        self.sponsor_without_user.delete()
        self.user.delete()
        self.category.delete()

    def test_should_request_and_be_success(self):
        self.assertEqual(200, self.response.status_code)

    def test_should_contains_sponsor_on_context(self):
        self.assertIn(self.sponsor, self.response.context['cl'].result_list)

    def test_should_not_has_sponsor_without_user_on_context(self):
        self.assertNotIn(self.sponsor_without_user, self.response.context['cl'].result_list)

    def test_should_contain_all_sponsors_if_user_is_superuser(self):
        self.user.is_superuser = True
        self.user.save()

        response = self.client.get('/admin/sponsors/sponsor/')

        self.assertIn(self.sponsor, response.context['cl'].result_list)
        self.assertIn(self.sponsor_without_user, response.context['cl'].result_list)

    def test_should_not_has_user_field_if_user_is_sponsors_user(self):
        response = self.client.get('/admin/sponsors/sponsor/%d/' % self.sponsor.id)
        form = response.context[0]['adminform'].form
        self.assertNotIn('user', form.fields.keys())

    def test_should_have_user_field_if_user_is_not_sponsors_user(self):
        self.client.get('/admin/sponsors/sponsor/%d/' % self.sponsor.id)
        self.sponsor.user = None
        self.sponsor.save()
        self.user.is_superuser = True
        self.user.save()

        response = self.client.get('/admin/sponsors/sponsor/%d/' % self.sponsor.id)
        form = response.context[0]['adminform'].form
        self.assertIn('user', form.fields.keys())

    def test_access_admin_with_superuser_after_access_add_sponsor_with_sponsors_user_should_have_user_field(self):
        self.client.get('/admin/sponsors/sponsor/%d/' % self.sponsor.id)
        self.sponsor.user = None
        self.sponsor.save()
        self.user.is_superuser = True
        self.user.save()

        response = self.client.get('/admin/sponsors/sponsor/add/')

        form = response.context[0]['adminform'].form
        self.assertIn('user', form.fields.keys())

    def test_add_new_sponsor_should_return_200(self):
        data = {"name":"test123",
                "description_en_us":"desctest",
                "url":"http://urlteste.com",
                "category":self.category.id,
                "user":self.user.id,
                "contact_set-MAX_NUM_FORMS": "",
                "contact_set-TOTAL_FORMS": "0",
                "contact_set-INITIAL_FORMS": "0"}

        self.user.is_superuser = True
        self.user.save()

        response = self.client.post('/admin/sponsors/sponsor/add/', data)
        self.assertEqual(200, response.status_code)
