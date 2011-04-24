import unittest
from datetime import date
from django.db import IntegrityError
from mittun.events.models import Event
from nose.tools import raises, assert_equals

class EventTestCase(unittest.TestCase):
    def setUp(self):
        self.event = Event.objects.create(name="Evento teste",date=date.today())

    def test_should_save_successfully_an_valid_event(self):
        event = Event(name="", description="Teste", url="none.com", date=date.today(), location="Home", address="Whatever Street, 1542")
        event.save()

    @raises(IntegrityError)
    def test_should_not_save_with_an_invalid_event(self):
        event = Event(name="", description="Teste", url="none.com", location="Home", address="Whatever Street, 1542")
        event.save()

    @raises(IntegrityError)
    def test_should_not_save_without_a_name(self):
        event = Event(name=None, description="Teste", date=date.today(), location="Home", address="Whatever Street, 1542")
        event.save()

    def test_should_return_the_name_of_the_event_when_call_an_event_directly(self):
        assert_equals(self.event.__unicode__(), "Evento teste")
