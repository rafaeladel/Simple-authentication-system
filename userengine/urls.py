from django.conf.urls import patterns, url
from userengine.views import start, signin, register, success, show_register

urlpatterns = patterns('',
				url("^signin/$", signin),
				url("^register/$", show_register),
				url("^register_process/$", register),
				url("^success/$", success),
			)
