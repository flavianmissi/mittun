from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from models import Event

def index(request):
    events = Event.objects.all()
    return render_to_response('index.html', {'events' : events})

def event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render_to_response('event.html', {'event' : event})
