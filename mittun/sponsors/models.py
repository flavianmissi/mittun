from django.contrib.auth.models import User, Permission
from django.core.validators import MaxLengthValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from transmeta import TransMeta


class Contact(models.Model):

    type = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=100)
    sponsor = models.ForeignKey("Sponsor")

    def __unicode__(self):
        return '%s - %s' % (self.name, self.email)


class Category(models.Model):
    __metaclass__ = TransMeta

    name = models.CharField(max_length=120)
    priority = models.IntegerField()

    class Meta:
        translate = ('name', )

    def __unicode__(self):
        return self.name


class Sponsor(models.Model):
    __metaclass__ = TransMeta

    name = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField()
    category = models.ForeignKey(Category)
    logo = models.ImageField(upload_to='sponsors')
    user = models.ForeignKey(User, null=True, blank=True)

    class Meta:
        translate = ('description', )

    def __unicode__(self):
        return self.name


@receiver(post_save, sender=Sponsor)
def adicionar_permissoes(sender, **kwargs):
    user = kwargs['instance'].user
    if user:
        PERMISSIONS = ["change_sponsor", "delete_sponsor", "add_contact", "change_contact", "delete_contact", "add_job", "change_job", "delete_job"]
        permissions = Permission.objects.filter(codename__in=PERMISSIONS)
        user.is_staff = True
        user.user_permissions.add(*permissions)
        user.save()


class Responsibility(models.Model):
    description = models.TextField(validators=[MaxLengthValidator(100)])


class Requirement(models.Model):
    description = models.CharField(max_length=100)


class Bonus(models.Model):
    description = models.CharField(max_length=100)


class Job(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField(validators=[MaxLengthValidator(600)])
    web_site = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    company = models.ForeignKey(Sponsor)
    responsabilities = models.ForeignKey(Responsibility)
    requirements = models.ForeignKey(Requirement)
    bonuses = models.ForeignKey(Bonus)
