from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^decisions/$', 'hellodjango.views.decisions_view'),
	(r'^decisions/(\d+)/$', 'hellodjango.views.decisions_view'),
	(r'^decisions/(\d+)/buckets/$', 'hellodjango.views.buckets_view'),
	
    # Examples:
    # url(r'^$', 'hellodjango.views.home', name='home'),
    # url(r'^hellodjango/', include('hellodjango.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
	(r'^admin/', include(admin.site.urls)),

)
