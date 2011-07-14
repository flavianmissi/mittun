from django.shortcuts import render_to_response, get_object_or_404
from mittun.events.models import Event

def index(request):
    events = Event.objects.all()
    return render_to_response('index.html', {'events' : events})

def event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render_to_response('event.html', {'event' : event})

def add(request):
    if request.method == "POST":
        event = Event(request.POST)
        return render_to_response('add.html')
    else:
        return render_to_response('add.html')
