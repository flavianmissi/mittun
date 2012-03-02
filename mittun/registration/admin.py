# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns
from django.contrib import admin
from django.template import response

from mittun.registration import forms, helpers, models


class SubscriberAdmin(admin.ModelAdmin):

    def __init__(self, *args, **kwargs):
        super(SubscriberAdmin, self).__init__(*args, **kwargs)
        self.mail_sender = helpers.MailSender()

    def get_urls(self):
        urls = super(SubscriberAdmin, self).get_urls()
        custom_urls = patterns('',
            (r'^send-mail/$', self.admin_site.admin_view(self.show_mail_form))
        )
        return custom_urls + urls

    def show_mail_form(self, request):
        if request.method == "POST":
            return self.send_mail(request)

        context = {"form": forms.SendMailForm()}
        return response.TemplateResponse(request, "send_subscribers_mail.html", context)

    def send_mail(self, request):
        form = forms.SendMailForm(request.POST)

        if form.is_valid():
            subscribers = models.Subscriber.objects.all()
            recipients = [s.email for s in subscribers]
            self.mail_sender.send_mail(form.data["subject"], form.data["body"], recipients)
            context = {"subscribers": subscribers}
            return response.TemplateResponse(request, "subscribers_mail_sent.html", context)

        context = {"form": form}
        return response.TemplateResponse(request, "send_subscribers_mail.html", context)


if models.Subscriber not in admin.site._registry:
    admin.site.register(models.Subscriber, SubscriberAdmin)
