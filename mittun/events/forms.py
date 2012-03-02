from django.forms import ModelForm

from mittun.events.models import Event


class BootstrapForm(ModelForm):

    class Meta:
        model = Event
        exclude = ('slug',)
