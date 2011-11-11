#-*- coding: utf-8 -*-

from datetime import date

from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import RequestFactory, Client

from events.views import EventDetailView
from events.models import Event


class EventDetailsViewTestCase(TestCase):

    def setUp(self):
        self.request = RequestFactory().get('event_details')
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

    def test_details_view_should_use_event_detail_template(self):
        response = EventDetailView.as_view()(self.request, slug=self.event.slug)
        self.assertTrue('event_detail.html' in response.template_name)

    def test_context_object_must_be_called_event(self):
        response = EventDetailView.as_view()(self.request, slug=self.event.slug)
        self.assertTrue('event' in response.context_data.keys())

    def test_template_must_have_the_event_name_in_content(self):
        response = EventDetailView.as_view()(self.request, slug=self.event.slug)
        self.assertTrue(self.event.name in response.rendered_content)

    def test_template_must_have_the_event_date_in_content(self):
        response = EventDetailView.as_view()(self.request, slug=self.event.slug)
        self.assertTrue(self.event.date.strftime('%b. %d, %Y') in response.rendered_content)

    def test_template_must_have_the_event_description_in_content(self):
        response = EventDetailView.as_view()(self.request, slug=self.event.slug)
        self.assertTrue(self.event.description in response.rendered_content)

    def test_should_get_the_detail_page_with_a_non_fake_request_and_be_success(self):
        client = Client()
        response = client.get(reverse('event_detail', args=[self.event.slug]))
        self.assertEqual(response.status_code, 200)
