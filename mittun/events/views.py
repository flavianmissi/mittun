from django.views.generic import ListView, DetailView

from events.models import Event


class IndexView(ListView):

    model = Event
    template_name = 'index.html'
    context_object_name = 'events'


class EventDetailView(DetailView):
    model = Event
    template_name = 'event_detail.html'
