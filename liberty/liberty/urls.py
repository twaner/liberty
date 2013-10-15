from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^employeetest/', include('employee.urls', namespace="employee")),
    url(r'^clienttest/', include('client.urls', namespace="client")),
    # Examples:
    # url(r'^$', 'liberty.views.home', name='home'),
    # url(r'^liberty/', include('liberty.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:

)
