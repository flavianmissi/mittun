from mittun.tests.utils import ModelTestCase
from mittun.sponsors.models import Job

class JobModelTestCase(ModelTestCase):

    def test_job_should_have_title_field(self):
        self.assertIsFieldPresent("title", Job)

    def test_job_should_have_location_field(self):
        self.assertIsFieldPresent("location", Job)

    def test_job_should_have_description_field(self):
        self.assertIsFieldPresent("description", Job)

    def test_job_should_have_company_field(self):
        self.assertIsFieldPresent("company", Job)

    def test_job_should_have_web_site_field(self):
        self.assertIsFieldPresent("web_site", Job)

    def test_job_should_have_email_field(self):
        self.assertIsFieldPresent("email", Job)

