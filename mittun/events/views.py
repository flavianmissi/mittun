from django.views.generic import ListView, DetailView, CreateView

from events.models import Event
from events.forms import EventForm


class IndexView(ListView):

    model = Event
    template_name = 'index.html'
    context_object_name = 'events'


class CreateEvent(CreateView):

    template_name = 'add.html'
    form_class = EventForm


class EventsListView(ListView):
    model = Event
    template_name = 'events_list.html'
    context_object_name = 'events'


class EventDetailView(DetailView):
    model = Event
    template_name = 'event_detail.html'
