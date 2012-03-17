from django.db import models

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

    class Meta:
        translate = ('name', )

    def __unicode__(self):
        return self.name


class Sponsor(models.Model):
    __metaclass__ = TransMeta

    name = models.CharField(max_length=100)
    description = models.TextField(max_length=255)
    url = models.URLField()
    category = models.ForeignKey(Category)
    logo = models.ImageField(upload_to='sponsors')

    class Meta:
        translate = ('description', )

    def __unicode__(self):
        return self.name
