from django.forms import ModelForm
from mittun.events.models import Event

class EventForm(ModelForm):
    class Meta:
        model = Event
