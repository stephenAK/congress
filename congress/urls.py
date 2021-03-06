from django.conf.urls import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
   # url(r'^$', 'congress.views.host', name='home'),
    # url(r'^congress/', include('congress.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # 
    # Uncomment the next line to enable the admin:
     
    # url(r'^admin/(?P<templates>[\d\w]+)/(?P<admin>[\d\w]+)/(?P<pk>[\d]+)/print/', admin._print_detail),
     url(r'^reg/',include('reg.urls')),
     url(r'^admin/', include(admin.site.urls)),
     #url(r'^congress/',include('congress.urls')),
     url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root' : settings.STATIC_ROOT,}),
)
