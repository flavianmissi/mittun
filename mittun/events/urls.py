from django.conf.urls.defaults import patterns, url

from events.views import BootstrapView


urlpatterns = patterns('',
    url(r'^$', BootstrapView.as_view(), name='bootstrap'),
)
