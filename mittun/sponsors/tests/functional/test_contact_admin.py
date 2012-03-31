from django.test import TestCase, Client
from django.contrib.auth.models import User, Permission

from mittun.sponsors.models import Sponsor, Category, Contact


class ContactAdminTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user('siminino', 'siminino@simi.com', 'simipass')
        self.user.is_staff = True
        contact_permissions = Permission.objects.filter(codename__in=['add_contact', 'change_contact', 'delete_contact'])
        self.user.user_permissions.add(*contact_permissions)
        self.user.save()

        self.category = Category.objects.create(name="categorytest", priority=1)
        self.sponsor = Sponsor.objects.create(name="nametest",
                                              description="desctest",
                                              url="http://urlteste.com",
                                              category=self.category,
                                              user=self.user)

        self.sponsor2 = Sponsor.objects.create(name="nametest2",
                                              description="desctest2",
                                              url="http://urlteste.com2",
                                              category=self.category)
        self.contact = Contact.objects.create(type="typetest", name="nametest", email="emailtest@com", sponsor=self.sponsor)
        self.contact_without_user = Contact.objects.create(type="typetest2", name="nametest2", email="emailtest@com2", sponsor=self.sponsor2)
        self.client = Client()
        self.client.login(username='siminino', password='simipass')
        self.response = self.client.get('/admin/sponsors/contact/')

    def tearDown(self):
        self.contact.delete()
        self.sponsor.delete()
        self.category.delete()
        self.user.delete()

    def test_should_return_200(self):
        self.assertEquals(200, self.response.status_code)

    def test_should_contains_contact_on_context(self):
        self.assertIn(self.contact, self.response.context['cl'].result_list)

    def test_should_not_has_contanct_without_user_on_context(self):
        self.assertNotIn(self.contact_without_user, self.response.context['cl'].result_list)

    def test_should_contain_all_contacts_if_user_is_superuser(self):
        self.user.is_superuser = True
        self.user.save()

        response = self.client.get('/admin/sponsors/contact/')

        self.assertIn(self.contact, response.context['cl'].result_list)
        self.assertIn(self.contact_without_user, response.context['cl'].result_list)
