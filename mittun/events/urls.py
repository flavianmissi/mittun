from django.conf.urls.defaults import patterns

urlpatterns = patterns('',
    (r'^(?P<event_id>\d+)/?$', 'mittun.events.views.event'),
    (r'^(?P<event_id>\d+)/?$', 'mittun.events.views.event'),
    (r'^add/?$', 'mittun.events.views.add')
)
