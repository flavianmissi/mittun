from datetime import date
from django.test import TestCase
from nose.tools import assert_equals
from mittun.events.models import Event

class EventsViewsTestCase(TestCase):
    fixtures = ['events.json']

    def test_should_get_index_and_be_success(self):
        response = self.client.get('/index/')
        assert_equals(response.status_code, 200)

    def test_should_get_an_inexistent_event_and_get_an_404_status(self):
        response = self.client.get('/event/3')
        assert_equals(response.status_code, 404)

    def test_should_get_an_event_and_be_success(self):
        response = self.client.get('/event/1')
        assert_equals(response.status_code, 200)

    def test_should_get_add_page_and_be_success(self):
        response = self.client.get('events/add/')
        assert_equals(response.status_code, 200)

    def test_should_create_a_new_event(self):
        total = Event.objects.all().count()
        self.client.post('events/create/', {'name': 'Dojo', 'description': 'Dojo', 'date': date.today()})
        assert_equals(Event.objects.all().count(), total+1)
