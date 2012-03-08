from django.db import models
from transmeta import TransMeta


class Location(models.Model):

    title = models.CharField(max_length=150)
    event = models.ForeignKey("Event")
    address = models.CharField(max_length=255)


class Event(models.Model):
    __metaclass__ = TransMeta

    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)

    class Meta:
        translate = ('description',)

    def __unicode__(self):
        return self.name
