from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=120)


class Sponsor(models.Model):

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    url = models.URLField()
    category = models.ForeignKey(Category)
    logo = models.ImageField(upload_to='sponsors')
