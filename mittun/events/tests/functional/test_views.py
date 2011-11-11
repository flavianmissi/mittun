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
        response = self.client.get(reverse('event_detail', args=['absent-event']))
        self.assertEqual(response.status_code, 404)

    def test_should_get_an_event_and_be_success(self):
        response = self.client.get(reverse('event_detail', args=[self.event_slug]))
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
        self.assertGreater(Event.objects.all().count(), total)

    def test_should_get_event_details_page_and_be_success(self):
        response = self.client.get(reverse('event_detail', args=[self.event_slug]))
        self.assertEqual(200, response.status_code)

    def test_should_create_an_event_with_a_html_description_and_render_it_in_the_template(self):
       event = Event.objects.create(name='Dojo',
                                    description='<h2>Dojo</h2><p>Python Dojo</p>',
                                    date=date.today(),
                                    location='location',
                                    address='address',
                                    slug='python-dojo',
                                   )
       response = self.client.get(reverse('event_detail', args=[event.slug]))
       self.assertIn(event.description, response.content)
