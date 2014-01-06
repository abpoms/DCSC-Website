from django.conf.urls import patterns, url

from here import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^validate$', views.validate, name='validate'),

) #+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)