from datetime import date

from django.core.urlresolvers import reverse
from django.test import TestCase

from events.models import Event


class EventsViewsTestCase(TestCase):

    fixtures = ['events.json']

    def test_should_get_index_and_be_success(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_should_get_an_inexistent_event_and_get_an_404_status(self):
        response = self.client.get(reverse('view_event', args=[3]))
        self.assertEqual(response.status_code, 404)

    def test_should_get_an_event_and_be_success(self):
        response = self.client.get(reverse('view_event', args=[1]))
        self.assertEqual(response.status_code, 200)

    def test_should_get_add_page_and_be_success(self):
        response = self.client.get(reverse('add_event'))
        self.assertEqual(response.status_code, 200)

    def test_should_create_a_new_event(self):
        total = Event.objects.all().count()

        post_data = {
            'name': 'Dojo',
            'description': 'Dojo',
            'date': date.today(),
            'location': 'location',
            'address': 'address',
            'slug': 'foo-bar',
        }

        self.client.post(reverse('add_event'), post_data)
        self.assertEqual(Event.objects.all().count(), total+1)

    def test_should_get_event_details_page_and_be_success(self):
        response = self.client.get(reverse('view_event'), args=[Event.objects.all()[0].id])
        self.assertEqual(200, response.status_code)
