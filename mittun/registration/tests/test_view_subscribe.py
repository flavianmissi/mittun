# -*- coding: utf-8 -*-
from django import http, test
from django.template import response
from django.test import client
from django.views.generic import base

from registration import forms, models, views


class SubscribeViewTestCase(test.TestCase):

    def setUp(self):
        factory = client.RequestFactory()
        self.request = factory.get("/subscribe")
        self.view = views.Subscribe()

    def test_should_store_a_success_url(self):
        view = views.Subscribe(success_url="/teste/")
        self.assertEqual("/teste/", view.success_url)

    def test_should_use_a_default_value_for_success_url(self):
        view = views.Subscribe()
        self.assertEqual("/successful-subscribed/", view.success_url)

    def test_should_extend_base_View(self):
        assert issubclass(views.Subscribe, base.View)

    def test_get_method_should_return_a_TemplateResponse_instance(self):
        r = self.view.get(self.request)
        self.assertIsInstance(r ,response.TemplateResponse)

    def test_get_method_should_render_the_template_name_variable_when_present(self):
        self.view.template_name = "my_subscribe.html"
        r = self.view.get(self.request)
        self.assertEqual("my_subscribe.html", r.template_name)

    def test_get_method_should_render_the_subscribe_html_template_when_template_name_is_not_present(self):
        r = self.view.get(self.request)
        self.assertEqual("subscribe.html", r.template_name)

    def test_get_method_should_include_a_SubscriptionForm_instance_in_the_context(self):
        r = self.view.get(self.request)
        form = r.context_data["form"]
        self.assertIsInstance(form, forms.SubscriberForm)


class SubscribeViewWithInvalidDataTestCase(test.TestCase):

    def setUp(self):
        self.data = {
            "name": "",
            "email": "francisco@mittun.com",
        }
        factory = client.RequestFactory()
        self.request = factory.post("/subscribers", self.data)
        self.view = views.Subscribe()

    def test_should_return_TemplateResponse(self):
        r = self.view.post(self.request)
        self.assertIsInstance(r, response.TemplateResponse)

    def test_should_include_the_failed_form_in_the_context(self):
        r = self.view.post(self.request)
        key_function = lambda x: x[0]
        expected = sorted(self.data.items(), key=key_function)
        got = sorted(r.context_data["form"].data.items(), key=key_function)
        self.assertEqual(expected, got)

    def test_should_render_the_template_name_variable_when_present(self):
        self.view.template_name = "my_subscribe.html"
        r = self.view.post(self.request)
        self.assertEqual("my_subscribe.html", r.template_name)

    def test_should_render_subscription_html_when_the_variable_template_name_is_not_present(self):
        r = self.view.post(self.request)
        self.assertEqual("subscribe.html", r.template_name)


class SubscribeWithValidDataTestCase(test.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data = {
            "name": u"Francisco Souza",
            "email": u"francisco@mittun.com",
        }

        factory = client.RequestFactory()
        request = factory.post("/subscribe", cls.data)
        cls.view = views.Subscribe()
        cls.response = cls.view.post(request)

    @classmethod
    def tearDownClass(cls):
        models.Subscriber.objects.get(**cls.data).delete()

    def test_should_create_the_subscriber_in_the_database(self):
        subscriber = models.Subscriber.objects.get(**self.data)
        self.assertEqual(u"Francisco Souza", subscriber.name)
        self.assertEqual(u"francisco@mittun.com", subscriber.email)

    def test_should_return_a_HttpResponseRedirect(self):
        self.assertIsInstance(self.response, http.HttpResponseRedirect)

    def test_should_redirect_to_the_success_url(self):
        self.assertEqual(self.view.success_url, self.response['Location'])
