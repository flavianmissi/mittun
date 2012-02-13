# -*- coding: utf-8 -*-
from django import test, forms as django_forms

from registration import forms


class SendMailFormTestCase(test.TestCase):

    def test_should_be_a_simple_form(self):
        assert issubclass(forms.SendMailForm, django_forms.Form)

    def test_should_have_a_subject_field(self):
        self.assertIn("subject", forms.SendMailForm.base_fields)

    def test_subject_should_be_a_CharField(self):
        field = forms.SendMailForm.base_fields["subject"]
        self.assertIsInstance(field, django_forms.CharField)

    def test_subject_should_have_at_most_300_characters(self):
        field = forms.SendMailForm.base_fields["subject"]
        self.assertEqual(300, field.max_length)

    def test_should_have_a_body_field(self):
        self.assertIn("body", forms.SendMailForm.base_fields)

    def test_body_should_be_a_CharField(self):
        field = forms.SendMailForm.base_fields["body"]
        self.assertIsInstance(field, django_forms.CharField)

    def test_body_should_have_at_most_5000_characters(self):
        field = forms.SendMailForm.base_fields["body"]
        self.assertEqual(5000, field.max_length)

    def test_body_should_use_the_Textarea_widget(self):
        field = forms.SendMailForm.base_fields["body"]
        self.assertIsInstance(field.widget, django_forms.Textarea)
