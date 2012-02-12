# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns
from django.contrib import admin
from django.template import response

from registration import forms, models


class SubscriberAdmin(admin.ModelAdmin):

    def get_urls(self):
        urls = super(SubscriberAdmin, self).get_urls()
        custom_urls = patterns('',
            (r'^send-mail/$', self.admin_site.admin_view(self.send_mail))
        )
        return custom_urls + urls

    def send_mail(self, request):
        context = {"subscribers": models.Subscriber.objects.all(), 'form': forms.SendMailForm()}
        return response.TemplateResponse(request, "send_subscribers_mail.html", context)

admin.site.register(models.Subscriber, SubscriberAdmin)
