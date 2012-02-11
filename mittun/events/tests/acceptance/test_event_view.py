from django.utils.unittest import TestCase
from events.management.browser_helper import browser



class EventViewTestCase(TestCase):

    def setUp(self):
        self.base_url = "http://localhost:8000"

    def test_should_visit_the_bootstrap_page_and_be_success(self):
        browser.visit('%s/bootstrap' % self.base_url)
        self.assertEqual(200, browser.status_code)
