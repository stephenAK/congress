from django.conf.urls.defaults import *
import views


urlpatterns = patterns('',
                  url(r'^$', 'reg.views.home'),
                  url(r'^guest/$', 'reg.views.guest'),
                  url(r'^host/$', 'reg.views.host'),
                  url(r'^alumni/$', 'reg.views.alumni'),
                  url(r'^congress/(?P<id>\d+)/((?P<showDetails>.*)/)?$', 'reg.views.post_detail'),
		  url(r'^congresshost/(?P<id>\d+)/((?P<hostsDetails>.*)/)?$', 'reg.views.host_detail'),
                  url(r'^congress/search/(?P<term>.*?)$','reg.views.post_search'),
		  url(r'^congress/searchost/(?P<term>.*?)$','reg.views.host_search'),
		  #url(r'^list/$', views.notes_list, name='notes_list'),
                )
