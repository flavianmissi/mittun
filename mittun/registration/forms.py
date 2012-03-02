# -*- coding: utf-8 -*-
from django import forms

from mittun.registration import models


class SendMailForm(forms.Form):
    subject = forms.CharField(max_length=300)
    body = forms.CharField(max_length=5000, widget=forms.Textarea())


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = models.Subscriber
        exclude = ('subscription_date',)
