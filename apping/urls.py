from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^apps/$', 'apps.views.index'),
	url(r'^apps/(?P<application_id>\d+)/$', 'apps.views.detail'),
#    url(r'^polls/(?P<poll_id>\d+)/results/$', 'polls.views.results'),
 #   url(r'^polls/(?P<poll_id>\d+)/vote/$', 'polls.views.vote'),
    # url(r'^apping/', include('apping.foo.urls')),

    	# Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
