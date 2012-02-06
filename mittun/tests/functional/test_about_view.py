#-*- coding: utf-8 -*-

from datetime import date

from django.test import TestCase
from django.test.client import RequestFactory

from events.views import EventDetailView
from events.models import Event


class EventDetailsViewTestCase(TestCase):

    def setUp(self):
        self.request = RequestFactory().get('abouts')
        self.event = Event.objects.create(
            name= 'Dojo',
            description= 'Dojo is a ...',
            date= date.today(),
            location= 'location',
            address= 'address'
        )

    def tearDown(self):
        self.event.delete()

    def test_should_request_the_details_view_and_get_an_200_status_code(self):
        response = EventDetailView.as_view()(self.request, slug=self.event.slug)
        self.assertEqual(response.status_code, 200)

    def test_details_view_should_use_about_template(self):
        response = EventDetailView.as_view()(self.request, slug=self.event.slug)
        self.assertTrue('about.html' in response.template_name)

    def test_context_object_must_be_called_event(self):
        response = EventDetailView.as_view()(self.request, slug=self.event.slug)
        self.assertTrue('event' in response.context_data.keys())

    def text_context_object_must_have_an_instance_of_event_model(self):
        response = EventDetailView.as_view()(self.request, slug=self.event.slug)
        self.assertIsInstance(response.context_data['event'], Event)
