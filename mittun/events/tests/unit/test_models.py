from datetime import date
from nose.tools import raises

from django.db import IntegrityError
from django.db import models

from mittun.events.models import Event
from mittun.tests.utils import ModelTestCase


class EventsModelsTestCase(ModelTestCase):
    fixtures = ['events.json']

    def test_should_have_the_field_name(self):
        self.assertIsFieldPresent('name', Event)

    def test_should_have_the_field_slug(self):
        self.assertIsFieldPresent('slug', Event)

    def test_should_have_the_field_description_for_english(self):
        self.assertIsFieldPresent('description_en_us', Event)

    def test_should_have_the_field_description_for_portuguese(self):
        self.assertIsFieldPresent('description_pt_br', Event)

    def test_should_have_the_field_date(self):
        self.assertIsFieldPresent('date', Event)

    def test_should_have_a_logo_field(self):
        self.assertIsFieldPresent('logo', Event)

    @raises(IntegrityError)
    def test_should_not_save_without_an_event_date(self):
        event = Event(name="", description_en_us="Teste")
        event.save()

    @raises(IntegrityError)
    def test_should_not_save_without_a_name(self):
        event = Event(name=None, description_en_us="Teste", date=date.today())
        event.save()

    def test_should_return_the_name_of_the_event_when_call_an_event_directly(self):
        event = Event.objects.get(pk=1)
        self.assertEqual(event.__unicode__(), event.name)

    def test_should_return_event_bar_the_event_name_when_asked_for_the_absolute_url_of_an_event(self):
        event = Event.objects.get(pk=1)
        expected_url = 'event/%s' % event.slug
        self.assertEqual(expected_url, event.get_absolute_url())

    def test_should_record_the_description_in_a_text_area(self):
        event = Event.objects.get(pk=1)
        self.assertIsInstance(event._meta._name_map['description_en_us'][0], models.TextField)
