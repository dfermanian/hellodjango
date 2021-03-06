from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^login/$', 'hellodjango.views.login_view'),
	(r'^decisions/$', 'hellodjango.views.decision_view'),
	(r'^decisions/(\d+)/$', 'hellodjango.views.decision_view'),
	(r'^decisions/(\d+)/buckets/$', 'hellodjango.views.bucket_view'),
	(r'^buckets/(\d+)/$', 'hellodjango.views.bucket_view'),
	(r'^customers/(\d+)/$', 'hellodjango.views.customer_view'),
	(r'^services/savebuckets$', 'hellodjango.services.savebuckets'),
	(r'^services/moveitem$', 'hellodjango.services.moveitem'),
	(r'^services/additem$', 'hellodjango.services.additem'),
	(r'^services/copyitem$', 'hellodjango.services.copyitem'),
	(r'^services/addbucket$', 'hellodjango.services.addbucket'),
	(r'^expanded_view/$', 'hellodjango.views.expanded_view'),
	(r'^expanded_view/(\d+)/$', 'hellodjango.views.expanded_view'),
	#(r'^services/addbucket$', 'hellodjango.services.addbucket'),

	
    # Examples:
    # url(r'^$', 'hellodjango.views.home', name='home'),
    # url(r'^hellodjango/', include('hellodjango.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
	(r'^admin/', include(admin.site.urls)),

)
