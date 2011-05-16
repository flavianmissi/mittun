from django.test import TestCase
from nose.tools import assert_equals

class EventsViewsTestCase(TestCase):
    fixtures = ['events.json']

    def test_should_get_index_and_be_success(self):
        response = self.client.get('index')
        assert_equals(response.status_code, 200)

    def test_should_get_an_inexistent_event_and_get_an_404_status(self):
        response = self.client.get('event/11359')
        assert_equals(response.status_code, 404)
