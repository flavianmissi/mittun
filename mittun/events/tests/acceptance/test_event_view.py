from django.utils.unittest import TestCase

from events.management.browser_helper import browser
from events.models import Event


class EventViewTestCase(TestCase):

    def setUp(self):
        self.base_url = "http://localhost:8000"

    def test_should_visit_the_bootstrap_page_and_be_success(self):
        browser.visit('%s/bootstrap' % self.base_url)
        self.assertEqual(200, browser.status_code)

    def test_should_add_an_event(self):
        events_count = Event.objects.all().count()
        browser.visit('%s/bootstrap' % self.base_url)
        browser.fill('name', 'a really cool event')
        browser.fill('description', 'this is a really cool event')
        browser.fill('date', '10/02/10')
        browser.fill('location', 'neverland')
        browser.fill('address', 'neverland, 1')
        browser.find_by_name('save').first.click()
        self.assertGreater(Event.objects.all().count(), events_count)
        Event.objects.filter(name='a really cool event').delete()
