from django.conf.urls import patterns, url
from userengine.views import signin, register, success

urlpatterns = patterns('',
				url("^$", signin),
				url("^register/$", register),				
				url("^success/$", success),
			)
