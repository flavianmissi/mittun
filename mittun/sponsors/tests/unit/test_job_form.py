from django.utils import unittest
from django.forms import ModelMultipleChoiceField

from sponsors.models import Job
from sponsors.forms import JobForm


class JobFormTest(unittest.TestCase):

    def test_job_form_should_be_a_form_for_job_model(self):
        self.assertEqual(Job, JobForm._meta.model)

    def test_job_form_shoulb_have_the_responsabilities_field_as_ModelMultipleChoiceField_intance(self):
        form = JobForm()
        self.assertEqual(ModelMultipleChoiceField, form.fields['responsabilities'].__class__)

