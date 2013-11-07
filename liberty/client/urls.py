from django.conf.urls import patterns, url
from client import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<client_id>\d+)/$',
        views.detail, name='detailedClient'),
    url(r'^addclient', views.addclient, name='addclient'),
)