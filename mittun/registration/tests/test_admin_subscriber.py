# -*- coding: utf-8 -*-
from django import test
from django.contrib import admin as django_admin
from django.core import management
from django.template import response
from django.test import client

from registration import admin, forms, models


class AdminSubscriberTestCase(test.TestCase):

    def test_Subscriber_model_should_be_registered_within_the_admin(self):
        self.assertIn(models.Subscriber, django_admin.site._registry)

    def test_Subscriber_model_should_be_registered_using_the_SubscriberAdmin_class(self):
        self.assertIsInstance(django_admin.site._registry[models.Subscriber], admin.SubscriberAdmin)


class AdminSubscriberSendMailViewTestCase(test.TestCase):

    @classmethod
    def setUpClass(cls):
        factory = client.RequestFactory()
        request = factory.get("/admin/registration/subscriber/send-mail")

        cls.admin = admin.SubscriberAdmin(models.Subscriber(), None)
        cls.response = cls.admin.show_mail_form(request)

    def test_should_have_a_view_to_send_email_to_all_subscribers(self):
        assert hasattr(self.admin, "show_mail_form")

    def test_show_mail_form_view_should_return_a_TemplateResponse(self):
        self.assertIsInstance(self.response, response.TemplateResponse)

    def test_show_mail_form_view_should_render_the_send_subscribers_email(self):
        self.assertEquals("send_subscribers_mail.html", self.response.template_name)

    def test_should_include_a_SendMailForm_instance_in_the_context(self):
        context = self.response.context_data
        self.assertIsInstance(context["form"], forms.SendMailForm)


class AdminSubscriberSendMailPostInvalidDataTestCase(test.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data = {
            "subject": "Welcome to the Django",
            "body": "",
        }

        factory = client.RequestFactory()
        request = factory.post("/admin/registration/subscriber/send-mail", cls.data)
        cls.admin = admin.SubscriberAdmin(models.Subscriber(), None)
        cls.response = cls.admin.show_mail_form(request)

    def test_should_return_a_TemplateResponse_instance(self):
        self.assertIsInstance(self.response, response.TemplateResponse)

    def test_should_render_the_same_template(self):
        self.assertEqual("send_subscribers_mail.html", self.response.template_name)

    def test_should_include_the_form_filled_up_with_the_fields_contents(self):
        form = self.response.context_data["form"]
        key_function = lambda x: x[0]
        expected = sorted(self.data.items(), key=key_function)
        got = sorted(form.data.items(), key=key_function)
        self.assertEquals(expected, got)


class AdminSubscriberSendMailWithValidData(test.TestCase):

    @classmethod
    def setUpClass(cls):
        management.call_command("loaddata", "subscribers.yaml", verbosity=0)

        cls.data = {
            "subject": "Welcome to the Django",
            "body": "Now die",
        }
        cls.sent = False

        def send(subject, receivers, body):
            cls.sent = True

        factory = client.RequestFactory()
        request = factory.post("/admin/registration/subscriber/send-mail", cls.data)
        cls.admin = admin.SubscriberAdmin(models.Subscriber.objects.get(pk=1), None)
        cls.admin.mail_sender.send_mail = send
        cls.response = cls.admin.show_mail_form(request)

    @classmethod
    def tearDownClass(cls):
        management.call_command("flush", verbosity=0, interactive=False)

    def test_should_send_the_mail_using_the_mail_sender(self):
        self.assertTrue(self.sent)

    def test_should_return_a_TemplateResponse_instance(self):
        self.assertIsInstance(self.response, response.TemplateResponse)

    def test_should_render_the_subscriber_mail_sent_template(self):
        self.assertEqual("subscribers_mail_sent.html", self.response.template_name)

    def test_should_include_all_subscribers_in_the_context(self):
        expected = list(models.Subscriber.objects.all())
        got = list(self.response.context_data["subscribers"])
        self.assertEqual(expected, got)
