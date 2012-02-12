# -*- coding: utf-8 -*-
from django.contrib import admin
from django.template import response

from registration import models


class SubscriberAdmin(admin.ModelAdmin):

    def send_mail(self, request):
        context = {"subscribers": models.Subscriber.objects.all()}
        return response.TemplateResponse(request, "send_subscribers_mail.html", context)

admin.site.register(models.Subscriber, SubscriberAdmin)
