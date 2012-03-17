from django.test import TestCase, RequestFactory, Client
from django.core.urlresolvers import reverse

from mittun.sponsors.views import SponsorsView


class SponsorsViewTestCase(TestCase):

    def setUp(self):
        self.request = RequestFactory().get('sponsors')
        self.response = SponsorsView.as_view()(self.request)

    def test_should_request_and_be_success(self):
        self.assertEqual(200, self.response.status_code)

    def test_should_use_sponsors_list_as_template_name(self):
        self.assertIn('sponsors_list.html', self.response.template_name)

    def test_should_get_the_url_and_be_success(self):
        response = Client().get(reverse('sponsors'))
        self.assertEqual(200, response.status_code)
