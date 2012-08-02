from django.test import TestCase, Client
from django.contrib.auth.models import User, Permission

from mittun.sponsors.models import Sponsor, Category, Job, Responsibility, Requirement, Bonus


class JobAdminTestCase(TestCase):

    @classmethod
    def setUpClass(self):
        self.user = User.objects.create_user('siminino', 'siminino@simi.com', 'simipass')
        job_permissions = Permission.objects.filter(codename__in=['add_job', 'change_job', 'delete_job'])
        self.user.user_permissions.add(*job_permissions)
        self.user.save()

        self.category = Category.objects.create(name="categorytest", priority=1)
        self.sponsor = Sponsor.objects.create(name="nametest",
                                              description="desctest",
                                              url="http://urlteste.com",
                                              category=self.category,
                                              user=self.user)

        self.sponsor2 = Sponsor.objects.create(name="nametest2",
                                              description="desctest2",
                                              url="http://urlteste.com2",
                                              category=self.category)

        self.job = Job.objects.create(title="titletest",
                                      location="locationtest",
                                      description="description test",
                                      company=self.sponsor,)

        self.job_without_user = Job.objects.create(title="titletest2",
                                      location="locationtest2",
                                      description="description test2",
                                      company=self.sponsor2,)

        self.client = Client()

    def setUp(self):
        self.user.is_superuser = False
        self.user.is_staff = True
        self.user.save()
        self.client.login(username='siminino', password='simipass')
        self.response = self.client.get('/admin/sponsors/job/')

    @classmethod
    def tearDownClass(self):
        self.job.delete()
        self.job_without_user.delete()
        self.sponsor.delete()
        self.sponsor2.delete()
        self.category.delete()
        self.user.delete()

    def test_should_return_200(self):
        self.assertEquals(200, self.response.status_code)

    def test_should_contains_job_on_context(self):
        self.assertIn(self.job, self.response.context['cl'].result_list)

    def test_should_not_has_job_without_user_on_context(self):
        self.assertNotIn(self.job_without_user, self.response.context['cl'].result_list)

    def test_should_contain_all_jobs_if_user_is_superuser(self):
        self.user.is_superuser = True
        self.user.save()

        response = self.client.get('/admin/sponsors/job/')

        self.assertIn(self.job, response.context['cl'].result_list)
        self.assertIn(self.job_without_user, response.context['cl'].result_list)
