from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import render_to_response, get_object_or_404

from events.models import Event
from events.forms import EventForm


def index(request):
    events = Event.objects.all()
    return render_to_response('index.html', {'events' : events})


def event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render_to_response('event.html', {'event' : event})


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
