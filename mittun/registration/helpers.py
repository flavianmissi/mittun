# -*- coding: utf-8 -*-

from django.core import mail


class MailSender(object):

    def build_message(self, subject, body, recipients):
        return mail.EmailMessage(subject, body, bcc=recipients)

    def send_mail(self, subject, body, recipients):
        message = self.build_message(subject, body, recipients)
        message.send(fail_silently=True)
        return message
