#-*- coding: utf-8 -*-

from django.test import TestCase
from django.test.client import RequestFactory

from mittun.views import AboutView
from mittun.events.models import Event


class AboutsViewTestCase(TestCase):

    def setUp(self):
        self.request = RequestFactory().get('about')
        self.event = Event.objects.create(
            name='Dojo',
            description='Dojo is a ...',
        )

    def tearDown(self):
        self.event.delete()

    def test_should_request_the_details_view_and_get_an_200_status_code(self):
        response = AboutView.as_view()(self.request)
        self.assertEqual(response.status_code, 200)

    def test_should_always_return_first_event_in_database(self):
        event2 = Event.objects.create(
            name='foo',
            description='bar',
        )

        response = AboutView.as_view()(self.request)
        self.assertIn(self.event, response.context_data().values())

        event2.delete()

    def test_details_view_should_use_about_template(self):
        response = AboutView.as_view()(self.request)
        self.assertIn('about.html', response.template_name)

    def test_context_object_must_be_called_event(self):
        response = AboutView.as_view()(self.request)
        self.assertIn('event', response.context_data().keys())

    def text_context_object_must_have_an_instance_of_event_model(self):
        response = AboutView.as_view()(self.request)
        self.assertIsInstance(response.context_data['event'], Event)
