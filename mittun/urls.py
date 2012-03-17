from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin

from mittun.views import IndexView, AboutView

admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', IndexView.as_view()),
    url(r'^index/?$', IndexView.as_view(), name="index"),
    url(r'^about/?$', AboutView.as_view(), name="about"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sponsors/?$', include('mittun.sponsors.urls')),
)

urlpatterns += staticfiles_urlpatterns()
