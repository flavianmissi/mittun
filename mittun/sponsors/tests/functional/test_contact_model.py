from mittun.tests.utils import ModelTestCase
from sponsors.models import Contact, Sponsor, Category


class ContactModelTestCase(ModelTestCase):

    def setUp(self):
        self.category = Category.objects.create(name='test')
        self.sponsor = Sponsor.objects.create(name='sponsor',
                                              description='description',
                                              url='someurl.com',
                                              category=self.category)
        self.contact = Contact.objects.create(type='contact type',
                                              name='contact name',
                                              email='contact email',
                                              sponsor=self.sponsor)

    def tearDown(self):
        self.category.delete()
        self.sponsor.delete()
        self.contact.delete()

    def test_should_have_a_type_field(self):
        self.assertIsFieldPresent('type', Contact)

    def test_should_have_a_name_field(self):
        self.assertIsFieldPresent('name', Contact)

    def test_should_have_an_email_field(self):
        self.assertIsFieldPresent('email', Contact)

    def test_should_have_a_sponsor_field(self):
        self.assertIsFieldPresent('sponsor', Contact)

    def test_should_return_contaact_name_and_email_when_called_by_unicode(self):
        self.assertEqual('%s - %s' % (self.contact.name, self.contact.email), unicode(self.contact))
