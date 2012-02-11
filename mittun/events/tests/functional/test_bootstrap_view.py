from django.test import TestCase, RequestFactory, Client
from django.core.urlresolvers import reverse

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
