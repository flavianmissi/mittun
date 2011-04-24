import unittest
from django.test.client import Client
from nose.tools import assert_equals

class EventsViewsTestCase(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_index(self):
        response = self.client.get('index/')
        assert_equals(response.status_code, 200)

    def test_event(self):
        response = self.client.get('event/11359')
        assert_equals(response.status_code, 404)
