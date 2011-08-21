# -*- coding: utf-8 -*-

from datetime import date
from nose.tools import assert_equals, assert_true

from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import RequestFactory, Client

from events.views import EventsListView
from events.models import Event


class EventsIndexViewTestCase(TestCase):

    def setUp(self):
        self.request = RequestFactory().get('events_list')
        self.event = Event.objects.create(
            name= 'Dojo',
            description= 'Dojo',
            date= date.today(),
            location= 'location',
            address= 'address'
        )

    def tearDown(self):
        self.event.delete()

    def test_should_get_the_index_and_get_a_200_status_code(self):
        response = EventsListView.as_view()(self.request)
        assert_equals(response.status_code, 200)

    def test_index_view_should_use_events_list_template(self):
        response = EventsListView.as_view()(self.request)
        assert_true('events_list.html' in response.template_name)

    def test_events_list_must_be_called_events_in_context(self):
        response = EventsListView.as_view()(self.request)
        assert_true('events' in response.context_data)

    def test_should_get_the_index_and_see_a_event_name(self):
        response = EventsListView.as_view()(self.request)
        assert_true(self.event.name in response.rendered_content)

    def test_should_get_the_index_with_all_events_names_listed(self):
        another_event = Event.objects.create(
            name= 'End of days',
            description= 'The end of days',
            date= date.today(),
            location= 'world',
            address= 'everywhere'
        )

        response = EventsListView.as_view()(self.request)

        assert_true(self.event.name in response.rendered_content)
        assert_true(another_event.name in response.rendered_content)

    def test_should_get_the_index_page_with_a_non_fake_request_and_be_success(self):
        client = Client()
        response = client.get(reverse('events_list'))
        assert_equals(response.status_code, 200)
