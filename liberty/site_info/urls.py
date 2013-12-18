from django.conf.urls import patterns, url
from site_info import views

urlpatterns = patterns('',
    #url(r'^$', views.index, name='index'),
    url(r'^(?P<site_id>\d+)/$',
        views.detail, name='detail'),
    url(r'index/$', views.index, name="index"),
    url(r'addsite/$', views.addsiteinfo, name="addsiteinfo"),

)