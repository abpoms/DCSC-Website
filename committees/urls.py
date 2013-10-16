from django.conf.urls import patterns, url

from committees import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<committee_abbreviation>\w+)$', views.detail, name='detail')
)
