from django.test import TestCase
from django.contrib import admin

from mittun.sponsors.models import Sponsor, Category, Contact
from mittun.sponsors.admin import SponsorAdmin, CategoryAdmin, ContactAdmin, ContactInline


class AdminTestCase(TestCase):

    def test_should_register_sponsor_model(self):
        self.assertIn(Sponsor, admin.site._registry)

    def test_should_register_sponsor_model_with_SponsorAdmin_class(self):
        self.assertIsInstance(admin.site._registry[Sponsor], SponsorAdmin)

    def test_should_register_category_model(self):
        self.assertIn(Category, admin.site._registry)

    def test_should_register_category_model_with_CategoryAdmin_class(self):
        self.assertIsInstance(admin.site._registry[Category], CategoryAdmin)

    def test_should_register_contact_model_with_ContactAdmin_class(self):
        self.assertIsInstance(admin.site._registry[Contact], ContactAdmin)


class ContactInlineTestCase(TestCase):

    def test_inline_should_have_a_model_attribute_with_the_Contact_model(self):
        self.assertEqual(Contact, ContactInline.model)

    def test_SponsorAdmin_should_have_ContactInline_in_inlines_list(self):
        self.assertIn(ContactInline, SponsorAdmin.inlines)
