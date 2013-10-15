from django.conf.urls import patterns, url
from employee import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='tester'),
    url(r'^(?P<employee_id>\d+)/$',
        views.detailed, name='detailed'),
    # ex employeetest/1/info

)