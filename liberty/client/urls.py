from django.conf.urls import patterns, url
from client import views

urlpatterns = patterns('',
    url(r'^$', views.clienttester, name='tester'),
    url(r'^(?P<client_id>\d+)/$',
        views.detailedClient, name='detailedClient'),


)