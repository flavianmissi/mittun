from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    url(r'^$', 'mittun.events.views.index', name="index"),
    url(r'^index/?$', 'mittun.events.views.index', name="index"),
    url(r'^events/', include('mittun.events.urls')),
)

urlpatterns += staticfiles_urlpatterns()
