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
        browser.fill('description', 'this is a really cool event')
        browser.fill('date', '10/02/10')
        browser.fill('location', 'neverland')
        browser.fill('address', 'neverland, 1')
        browser.find_by_name('save').first.click()

        self.assertGreater(Event.objects.all().count(), events_count)

        Event.objects.filter(name='a really cool event').delete()


class EditEventTestCase(BaseEventTestCase, TestCase):

    def setUp(self):
        Event.objects.create(
            name='some event',
            description='some description',
            date=datetime.now(),
            location='some location',
            address='some address'
        )
        super(EditEventTestCase, self).setUp()

    def test_should_edit_an_event(self):
        field_name = browser.find_by_name('name').first.value
        self.assertEqual('some event', field_name)
