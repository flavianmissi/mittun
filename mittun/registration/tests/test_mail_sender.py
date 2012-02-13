# -*- coding: utf-8 -*-
from django import test
from django.conf import settings
from django.core import mail

from registration import helpers


class EmailMessageMock(mail.EmailMessage):

    def __init__(self, *args, **kwargs):
        super(EmailMessageMock, self).__init__(*args, **kwargs)
        self.sent = False

    def send(self, fail_silently):
        if fail_silently:
            self.sent = True



class MailSenderTestCase(test.TestCase):

    def setUp(self):
        self.sender = helpers.MailSender()
        self.subject = u"Welcome to the Django"
        self.body = u"Now die"
        self.recipients = ["flaviamissi@gmail.com", "f@souza.cc"]
        self.email = self.sender.build_message(self.subject, self.body, self.recipients)

    def test_should_build_an_EmailMessage_instance(self):
        self.assertEqual(self.recipients, self.email.recipients())

    def test_should_use_the_setting_DEFAULT_FROM_EMAIL_as_the_email_sender(self):
        self.assertEqual(settings.DEFAULT_FROM_EMAIL, self.email.from_email)

    def test_should_send_the_email_using_the_EmailMessage_class(self):
        self.sender.build_message = lambda *args: EmailMessageMock(*args)
        message = self.sender.send_mail(self.subject, self.body, self.recipients)
        self.assertTrue(message.sent)
