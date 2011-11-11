from django.conf.urls.defaults import patterns, url
from events.views import EventsListView, EventDetailView, CreateEvent

urlpatterns = patterns('',
    url(r'^index/?$', EventsListView.as_view(), name="events_list"),
    url(r'^details/(?P<slug>[a-zA-Z-0-9\_]+)/?$', EventDetailView.as_view(), name="event_detail"),
    url(r'^add/?$', CreateEvent.as_view(), name="add_event"),
)
