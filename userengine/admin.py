from django.contrib import admin
from userengine.models import users

class usersAdmin(admin.ModelAdmin):
	list_display = ('username', 'hashed_password', 'email', 'last_login')
	list_filter = ('last_login',)
	search_fields = ("username",)
	

admin.site.register(users, usersAdmin)
