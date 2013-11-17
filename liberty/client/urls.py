from django.conf.urls import patterns, url
from client import views

urlpatterns = patterns('',
    url(r'^index', views.index, name='index'),
    url(r'^(?P<client_id>\d+)/$',
        views.detail, name='detail'),
    url(r'^addclient', views.addclient, name='addclient'),
    url(r'^addsalesprospect', views.addsalesprospect, name='addsalesprospect'),
    url(r'^salesprospectindex', views.salesprospectindex, name='salesprospectindex'),
    url(r'^salesprospectdetail/(?P<sales_prospect_id>\d+)/$',
        views.salesprospectdetails, name='salesprospectdetails'),
)