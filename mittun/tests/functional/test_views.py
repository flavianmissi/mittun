from datetime import date

from django.core.urlresolvers import reverse
from django.test import TestCase

from events.models import Event


class EventsViewsTestCase(TestCase):

    fixtures = ['events.json']

    def setUp(self):
        self.event_slug = Event.objects.all()[0].slug

    def test_should_get_index_and_be_success(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_should_get_an_inexistent_event_and_get_an_404_status(self):
        response = self.client.get(reverse('about', args=['absent-event']))
        self.assertEqual(response.status_code, 404)

    def test_should_get_an_event_and_be_success(self):
        response = self.client.get(reverse('about', args=[self.event_slug]))
        self.assertEqual(response.status_code, 200)

    def test_should_get_abouts_page_and_be_success(self):
        response = self.client.get(reverse('about', args=[self.event_slug]))
        self.assertEqual(200, response.status_code)
