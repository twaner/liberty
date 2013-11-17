from django.conf.urls import patterns, url
from employee import views

urlpatterns = patterns('',
    url(r'^$', views.indexer, name='indexer'),
    url(r'^(?P<employee_id>\d+)/$',
        views.details, name='details'),
    url(r'^search-form/$',
        views.search_form, name='search_form'),
    url(r'^search/$', views.search, name='search'),
    #url(r'^addemployee/$', views.addemployee, name='addemployee'),
    url(r'test/$', views.testing, name='testing'),
    url(r'index/$', views.indexer, name="index"),
    url(r'addemployee/$', views.addemployee, name='addemployee'),
    #url(r'addemployee/$', views.employeeform, name='employeeform'),
    url(r'title/$', views.titleform, name='titleform'),
    url(r'empform/$', views.empform, name='empform'),
)