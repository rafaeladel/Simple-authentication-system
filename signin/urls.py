from django.conf.urls import patterns, include, url
from django.contrib import admin
from userengine.views import start
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', start),
	url(r'', include('userengine.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
