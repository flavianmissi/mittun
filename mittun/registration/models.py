# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Subscriber(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    email = models.EmailField(max_length=255, unique=True, verbose_name=_("Email"))
    subscription_date = models.DateTimeField(auto_now_add=True, verbose_name=_("Subscription date"))

    def __unicode__(self):
        return self.name
