from django.conf.urls import patterns, url

from here import views

urlpatterns = patterns(
    '',
    # ex: /here/
    url(r'^$', views.index, name='index'),
)
