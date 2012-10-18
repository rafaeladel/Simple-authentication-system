from django.db import models
import datetime

class users(models.Model):
	username = models.CharField(max_length=50)
	hashed_password = models.CharField(max_length=200)
	email = models.CharField(max_length=100, blank=True)
	last_login = models.DateTimeField()
	
	def __unicode__(self):
		return self.username
