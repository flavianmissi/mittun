from datetime import datetime

from django.core.urlresolvers import reverse
from django.test import TestCase, RequestFactory, Client

from events.forms import BootstrapForm
from events.models import Event
from events.views import BootstrapView


class BootstrapViewTestCase(TestCase):

    def setUp(self):
        self.request = RequestFactory().get('bootstrap')

    def test_should_request_bootstrap_and_be_success(self):
        response = BootstrapView.as_view()(self.request)
        self.assertEqual(200, response.status_code)

    def test_should_have_a_model_property(self):
        self.assertTrue(hasattr(BootstrapView, 'model'))

    def test_should_point_to_event_model(self):
        self.assertEqual(BootstrapView.model, Event)

    def test_should_have_a_form_class_property(self):
        self.assertTrue(hasattr(BootstrapView, 'form_class'))

    def test_should_point_to_event_form(self):
        self.assertEqual(BootstrapView.form_class, BootstrapForm)


class BootstrapViewUrlsTestCase(TestCase):

    def setUp(self):
        client = Client()
        self.response = client.get(reverse('bootstrap'))

    def test_should_request_bootstrap_url_and_get_a_200_status_code(self):
        self.assertEqual(200, self.response.status_code)


class BootstrapEditViewTestCase(TestCase):

    def setUp(self):
        self.event = Event.objects.create(
            name='foo',
            description='bar',
            date=datetime.now(),
            location='foo',
            address='bar'
        )
        client = Client()
        self.response = client.get(reverse('bootstrap'))

    def tearDown(self):
        self.event.delete()

    def test_should_get_the_bootstrap_page_and_have_an_event_in_the_context(self):
        self.assertIn('event', self.response.context_data.keys())

    def test_should_get_the_bootstrap_page_get_a_rendered_event_to_edit(self):
        self.assertEqual(self.event.name, self.response.context_data['event'].name)
