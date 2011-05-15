from datetime import date
from django.db import IntegrityError
from mittun.events.models import Event
from nose.tools import raises, assert_equals
from unittest import TestCase

class EventsModelsTestCase(TestCase):
    fixtures = ['events.json']

    @raises(IntegrityError)
    def test_should_not_save_without_an_event_date(self):
        event = Event(name="", description="Teste", url="none.com", location="Home", address="Whatever Street, 1542")
        event.save()

    @raises(IntegrityError)
    def test_should_not_save_without_a_name(self):
        event = Event(name=None, description="Teste", date=date.today(), location="Home", address="Whatever Street, 1542")
        event.save()

    def test_should_return_the_name_of_the_event_when_call_an_event_directly(self):
        event = Event.objects.get(pk=1)
        assert_equals(event.__unicode__(), event.name)
