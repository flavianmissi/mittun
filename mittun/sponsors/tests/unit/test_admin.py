from django.test import TestCase
from django.contrib import admin

from sponsors.models import Sponsor, Category, Contact
from sponsors.admin import SponsorAdmin, CategoryAdmin, ContactAdmin


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
