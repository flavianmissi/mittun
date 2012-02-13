# coding: utf8

import os
from datetime import datetime

from django.utils.unittest import TestCase

from events.management.browser_helper import browser
from events.models import Event


class BaseEventTestCase(object):

    def setUp(self):
        self.base_url = "http://localhost:8000"
        browser.visit('%s/bootstrap' % self.base_url)


class EventViewTestCase(BaseEventTestCase, TestCase):

    def test_should_visit_the_bootstrap_page_and_be_success(self):
        self.assertEqual(200, browser.status_code)

    def test_should_add_an_event(self):
        events_count = Event.objects.all().count()
        browser.fill('name', 'a really cool event')
        browser.fill('description_en_us', 'this is a really cool event')
        browser.fill('date', '10/02/10')
        browser.attach_file('logo', os.path.abspath('events/tests/data/batcat.jpg'))
        browser.find_by_name('save').first.click()

        self.assertGreater(Event.objects.all().count(), events_count)

        Event.objects.filter(name='a really cool event').delete()


class EditEventTestCase(BaseEventTestCase, TestCase):

    def setUp(self):
        self.event = Event.objects.create(
            name='some event',
            description_en_us='some description',
            date=datetime.now(),
        )
        super(EditEventTestCase, self).setUp()

    def tearDown(self):
        self.event.delete()

    def test_should_edit_an_event(self):
        old_field_name = browser.find_by_name('name').first.value
        browser.fill('name', 'new event name')
        browser.find_by_name('save').first.click()
        new_event_name = browser.find_by_name('name').first.value

        self.assertNotEqual(new_event_name, old_field_name)
