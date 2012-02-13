from django.db.models.signals import pre_save
from django.db import models
from django.template.defaultfilters import slugify


class Location(models.Model):

    title = models.CharField(max_length=150)
    event = models.ForeignKey("Event")
    address = models.CharField(max_length=255)


class Event(models.Model):

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    date = models.DateField()
    slug = models.SlugField()
    logo = models.ImageField(upload_to='event_logo')

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return 'event/%s' % self.slug


def generate_slug(instance, *args, **kwargs):
    instance.slug = slugify(instance.name)


pre_save.connect(generate_slug, sender=Event)
