# -*- coding: utf-8 -*-
import unittest

from django import forms as django_forms

from registration import forms, models


class SubscriberFormTestCase(unittest.TestCase):

    def test_should_extend_ModelForm(self):
        assert issubclass(forms.SubscriberForm, django_forms.ModelForm)

    def test_should_use_Subscriber_as_model(self):
        self.assertEquals(models.Subscriber, forms.SubscriberForm.Meta.model)

    def test_should_exclude_subscription_date(self):
        self.assertIn("subscription_date", forms.SubscriberForm.Meta.exclude)
