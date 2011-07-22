from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'^(?P<event_id>\d+)/?$', 'mittun.events.views.event', name="view_event"),
    url(r'^add/?$', 'mittun.events.views.add', name="add_event")
)
