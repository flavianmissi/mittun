# -*- coding: utf-8 -*-
import unittest

from django.db import models as django_models

from registration import models


class SubscriberModelTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.field_names = models.Subscriber._meta.get_all_field_names()

    def test_should_have_a_name(self):
        self.assertIn("name", self.field_names)

    def test_name_should_be_a_CharField(self):
        field = models.Subscriber._meta.get_field_by_name("name")[0]
        self.assertIsInstance(field, django_models.CharField)

    def test_name_should_have_at_most_255_characters(self):
        field = models.Subscriber._meta.get_field_by_name("name")[0]
        self.assertEquals(255, field.max_length)

    def test_should_have_an_email(self):
        self.assertIn("email", self.field_names)

    def test_email_should_be_a_EmailField(self):
        field = models.Subscriber._meta.get_field_by_name("email")[0]
        self.assertIsInstance(field, django_models.EmailField)

    def test_email_should_have_at_most_255_characters(self):
        field = models.Subscriber._meta.get_field_by_name("email")[0]
        self.assertEquals(255, field.max_length)

    def test_should_have_a_subscription_date(self):
        self.assertIn("subscription_date", self.field_names)

    def test_subscription_date_should_be_a_DateTimeField(self):
        field = models.Subscriber._meta.get_field_by_name("subscription_date")[0]
        self.assertIsInstance(field, django_models.DateTimeField)

    def test_subscription_date_should_be_automatic_defined_on_creation(self):
        field = models.Subscriber._meta.get_field_by_name("subscription_date")[0]
        self.assertTrue(field.auto_now_add)

    def test__unicode__shoul_return_the_Subscriber_name(self):
        s = models.Subscriber(name=u"Mario")
        self.assertEquals(u"Mario", unicode(s))
        
