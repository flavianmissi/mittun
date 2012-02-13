from datetime import date
from django.db import IntegrityError
from mittun.events.models import Event
from nose.tools import raises, assert_equals
from django.test import TestCase


class EventsModelsTestCase(TestCase):
    fixtures = ['events.json']

    def test_should_have_the_field_name(self):
        self.assertFieldIn('name', Event)

    def test_should_have_the_field_slug(self):
        self.assertFieldIn('slug', Event)

    def test_should_have_the_field_description(self):
        self.assertFieldIn('description', Event)

    def test_should_have_the_field_url(self):
        self.assertFieldIn('url', Event)

    def test_should_have_the_field_date(self):
        self.assertFieldIn('date', Event)

    def test_should_have_the_field_address(self):
        self.assertFieldIn('address', Event)

    def assertFieldIn(self, field_name, model):
        self.assertIn(field_name, [field.name for field in model._meta.fields])

    @raises(IntegrityError)
    def test_should_not_save_without_an_event_date(self):
        event = Event(name="", description="Teste", url="none.com", address="Whatever Street, 1542")
        event.save()

    @raises(IntegrityError)
    def test_should_not_save_without_a_name(self):
        event = Event(name=None, description="Teste", date=date.today(), address="Whatever Street, 1542")
        event.save()

    def test_should_return_the_name_of_the_event_when_call_an_event_directly(self):
        event = Event.objects.get(pk=1)
        assert_equals(event.__unicode__(), event.name)

    def test_should_return_event_bar_the_event_name_when_asked_for_the_absolute_url_of_an_event(self):
        event = Event.objects.get(pk=1)
        expected_url = 'event/%s' % event.slug
        assert_equals(expected_url, event.get_absolute_url())
