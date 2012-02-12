from django.db import models


class Subscriber(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    subscribe_date = models.DateTimeField(auto_now_add=True)
