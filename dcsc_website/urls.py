from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

import dcsc_website.views

import committees.urls
import here.urls

urlpatterns = patterns(
    '',
    url(r'^$', dcsc_website.views.index, name='index'),
    url(r'^committees/', include(committees.urls, namespace='committees')),
    url(r'^here/', include('here.urls', namespace='here')),

    url(
        r'^media/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
