# -*- coding: utf-8 -*-
from django import test
from django.contrib import admin as django_admin

from registration import admin, models


class AdminSubscriberTestCase(test.TestCase):

    def test_model_Subscriber_should_be_registered_within_the_admin(self):
        self.assertIn(models.Subscriber, django_admin.site._registry)

    def test_Subscriber_model_should_be_registered_using_the_SubscriberAdmin_class(self):
        self.assertIsInstance(django_admin.site._registry[models.Subscriber], admin.SubscriberAdmin)
