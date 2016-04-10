from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^mongonaut/', include('mongonaut.urls')),

    url(r'^$', include('nameall.urls')),
    url(r'^nameall/', include('nameall.urls')),
)
