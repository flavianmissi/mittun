from nose.tools import raises

from django.db import IntegrityError
from django.db import models

from mittun.events.models import Event
from mittun.tests.utils import ModelTestCase


class EventsModelsTestCase(ModelTestCase):
    fixtures = ['events.json']

    def test_should_have_the_field_name(self):
        self.assertIsFieldPresent('name', Event)

    def test_should_have_the_field_description_for_english(self):
        self.assertIsFieldPresent('description_en_us', Event)

    def test_should_have_the_field_description_for_portuguese(self):
        self.assertIsFieldPresent('description_pt_br', Event)

    @raises(IntegrityError)
    def test_should_not_save_without_a_name(self):
        event = Event(name=None, description_en_us="Teste")
        event.save()

    def test_should_return_the_name_of_the_event_when_call_an_event_directly(self):
        event = Event.objects.get(pk=1)
        self.assertEqual(event.__unicode__(), event.name)

    def test_should_record_the_description_in_a_text_area(self):
        event = Event.objects.get(pk=1)
        self.assertIsInstance(event._meta._name_map['description_en_us'][0], models.TextField)
