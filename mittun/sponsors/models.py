from django.db import models


class Contact(models.Model):

    type = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=100)
    sponsor = models.ForeignKey("Sponsor")

    def __unicode__(self):
        return '%s - %s' % (self.name, self.email)


class Category(models.Model):

    name = models.CharField(max_length=120)

    def __unicode__(self):
        return self.name


class Sponsor(models.Model):

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    url = models.URLField()
    category = models.ForeignKey(Category)
    logo = models.ImageField(upload_to='sponsors')

    def __unicode__(self):
        return self.name
