# -*- coding: utf-8 -*-
from django import http
from django.template import response
from django.views.generic import base

from mittun.registration import forms


class SubscribeView(base.View):

    def __init__(self, *args, **kwargs):
        super(SubscribeView, self).__init__(*args, **kwargs)
        if not hasattr(self, "success_url"):
            self.success_url = "/successful-subscribed/"

    def get(self, request):
        template_name = getattr(self, "template_name", "subscribe.html")
        context = {"form": forms.SubscriberForm()}
        return response.TemplateResponse(request, template_name, context)

    def post(self, request):
        form = forms.SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            return http.HttpResponseRedirect(self.success_url)

        template_name = getattr(self, "template_name", "subscribe.html")
        context = {"form": form}
        return response.TemplateResponse(request, template_name, context)
