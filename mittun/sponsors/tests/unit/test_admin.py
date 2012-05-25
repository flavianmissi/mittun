from django.test import TestCase
from django.contrib import admin

from mittun.sponsors.models import Sponsor, Category, Contact, Job, Requirement, Responsibility, Bonus
from mittun.sponsors.admin import SponsorAdmin, ContactAdmin, ContactInline, JobAdmin, RequirementInline, ResponsibilityInline, BonusInline


class AdminTestCase(TestCase):

    def test_should_register_sponsor_model(self):
        self.assertIn(Sponsor, admin.site._registry)

    def test_should_register_sponsor_model_with_SponsorAdmin_class(self):
        self.assertIsInstance(admin.site._registry[Sponsor], SponsorAdmin)

    def test_should_register_category_model(self):
        self.assertIn(Category, admin.site._registry)

    def test_should_register_contact_model_with_ContactAdmin_class(self):
        self.assertIsInstance(admin.site._registry[Contact], ContactAdmin)

    def test_should_register_job_admin(self):
        self.assertIsInstance(admin.site._registry[Job], JobAdmin)

    def test_should_register_requirement_model(self):
        self.assertIn(Requirement, admin.site._registry)

    def test_should_register_responsibility_model(self):
        self.assertIn(Responsibility, admin.site._registry)

    def test_should_register_bonus_model(self):
        self.assertIn(Bonus, admin.site._registry)

    def test_job_admin_should_have_requirement_responsibilities_and_bonuses_as_inline_models(self):
        self.assertIn(RequirementInline, JobAdmin.inlines)
        self.assertIn(ResponsibilityInline, JobAdmin.inlines)
        self.assertIn(BonusInline, JobAdmin.inlines)


class ContactInlineTestCase(TestCase):

    def test_inline_should_have_a_model_attribute_with_the_Contact_model(self):
        self.assertEqual(Contact, ContactInline.model)

    def test_SponsorAdmin_should_have_ContactInline_in_inlines_list(self):
        self.assertIn(ContactInline, SponsorAdmin.inlines)
