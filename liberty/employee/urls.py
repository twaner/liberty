from django.conf.urls import patterns, url
from employee import views

urlpatterns = patterns('',
    url(r'^(?P<employee_id>\d+)/$',
        views.details, name='details'),
    #url(r'^search-form/$',
     #   views.search_form, name='search_form'),
    #url(r'^search/$', views.search, name='search'),
    url(r'index/$', views.index, name="index"),
    #url(r'addemployee/$', views.addemployee, name='addemployee'),
    url(r'title/$', views.titleform, name='titleform'),
    url(r'empform/$', views.empform, name='empform'),
    url(r'editemployee/(?P<employee_id>\d+)/$', views.editemployee,
        name='editemployee'),
    #r'^salesprospectdetail/(?P<sales_prospect_id>\d+)/$',
)