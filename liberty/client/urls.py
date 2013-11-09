from django.conf.urls import patterns, url
from client import views

urlpatterns = patterns('',
    url(r'^index', views.index, name='index'),
    url(r'^(?P<client_id>\d+)/$',
        views.detail, name='detail'),
    url(r'^addclient', views.addclient, name='addclient'),
)