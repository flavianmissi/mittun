# -*- coding: utf-8 -*-
from django.contrib import admin

from registration import models


class SubscriberAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Subscriber, SubscriberAdmin)
