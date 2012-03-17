from django.conf.urls.defaults import patterns, url

from mittun.sponsors.views import SponsorsView


urlpatterns = patterns('',
    url(r'^$', SponsorsView.as_view(), name='sponsors'),
)
