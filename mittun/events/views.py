from django.shortcuts import render_to_response, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect
from django.template import RequestContext
from mittun.events.models import Event
from mittun.events.forms import EventForm

def index(request):
    events = Event.objects.all()
    return render_to_response('index.html', {'events' : events})

def event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render_to_response('event.html', {'event' : event})

@csrf_protect
def add(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            print form.cleaned_data
            return HttpResponseRedirect('/')
    else:
        form = EventForm()

    return render_to_response('add.html', {'form': form}, context_instance=RequestContext(request))
