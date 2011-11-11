from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from events.views import IndexView


urlpatterns = patterns('',
    url(r'^$', IndexView.as_view()),
    url(r'^index/?$', IndexView.as_view(), name="index"),
    url(r'^events/', include('mittun.events.urls')),
)

urlpatterns += staticfiles_urlpatterns()
