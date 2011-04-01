from django.db import models

class Event(models.Model):
    description = models.CharField(max_length=200)
    date = models.DateField()
    location = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
