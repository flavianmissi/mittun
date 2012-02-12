# -*- coding: utf-8 -*-
from django import forms

from registration import models


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = models.Subscriber
        exclude = ('subscription_date',)
