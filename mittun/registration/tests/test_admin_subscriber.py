# -*- coding: utf-8 -*-
from django import test
from django.contrib import admin as django_admin
from django.core import management
from django.template import response
from django.test import client

from registration import admin, models


class AdminSubscriberTestCase(test.TestCase):

    def test_Subscriber_model_should_be_registered_within_the_admin(self):
        self.assertIn(models.Subscriber, django_admin.site._registry)

    def test_Subscriber_model_should_be_registered_using_the_SubscriberAdmin_class(self):
        self.assertIsInstance(django_admin.site._registry[models.Subscriber], admin.SubscriberAdmin)


class AdminSubscriberSendMailViewTestCase(test.TestCase):

    @classmethod
    def setUpClass(cls):
        management.call_command("loaddata", "subscribers.yaml", verbosity=0)

        factory = client.RequestFactory()
        request = factory.get("/admin/registration/subscriber/send-mail")

        cls.admin = admin.SubscriberAdmin(models.Subscriber.objects.get(pk=1), None)
        cls.response = cls.admin.send_mail(request)

    @classmethod
    def tearDownClass(cls):
        management.call_command("flush", interactive=False, verbosity=0)

    def test_should_have_a_view_to_send_email_to_all_subscribers(self):
        assert hasattr(self.admin, "send_mail")

    def test_send_mail_view_should_return_a_TemplateResponse(self):
        self.assertIsInstance(self.response, response.TemplateResponse)

    def test_send_mail_view_should_render_the_send_subscribers_email(self):
        self.assertEquals("send_subscribers_mail.html", self.response.template_name)

    def test_should_render_the_template_with_all_subscribers_in_the_context(self):
        context = self.response.context_data
        self.assertEquals(list(models.Subscriber.objects.all()), list(context["subscribers"]))
