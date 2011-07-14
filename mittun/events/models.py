from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    url = models.CharField(max_length=250, blank=True)
    date = models.DateField()
    location = models.CharField(max_length=100)
    address = models.CharField(max_length=250)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return 'event/%i' % self.id
