from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.core.urlresolvers import reverse
from userengine.models import users
from django.core.exceptions import ObjectDoesNotExist
import hashlib
import datetime
from validation import validate

def start(request):
	return render_to_response("signin.html", context_instance=RequestContext(request) )

def signin(request):
	password = hashlib.sha256(request.POST["password"]).hexdigest()
	try:
		current_user = users.objects.get(username=request.POST["username"])
	except (KeyError, ObjectDoesNotExist):
		return render_to_response("signin.html", {"error_message": "User does not exist"}, context_instance=RequestContext(request))
	else:
		if(current_user.hashed_password == password):
			current_user.last_login = datetime.datetime.now()
			current_user.save()
			return HttpResponseRedirect(reverse("userengine.views.success"))
		else:
			return render_to_response("signin.html", {"error_message": "Invalid password"}, context_instance=RequestContext(request))

def show_register(request):
	return render_to_response("register.html", context_instance=RequestContext(request))

def getBack(request, error_message=""):
	return render_to_response("register.html", {
								"username":request.POST.get("username",""),
								"password":request.POST.get("password",""),
								"password_again":request.POST.get("password_again",""),
								"email":request.POST.get("email",""),
								"error_message":error_message
								},context_instance=RequestContext(request))

def register(request):
	if not validate(request.POST["username"]):
		return getBack(request, error_message = "Invalid username.")		
	
	if not validate(request.POST["password"]):
		return getBack(request, error_message = "Invalid password.")		
		
	if request.POST["password"] != request.POST["password_again"]:
		return getBack(request, error_message = "Password confirmation didn't match!")		
	
	exists = users.objects.filter(username__exact= request.POST["username"])
	if exists:
		return getBack(request, error_message = "User already exists")		
	else:		
		password = hashlib.sha256(request.POST["password"]).hexdigest()
		new_user = users(username = request.POST["username"],
						hashed_password = password,
						email = request.POST.get("email",""),
						last_login = datetime.datetime.now())
		new_user.save()
		return render(request, "signin.html",{"error_message":"New user added."})
		
                

def success(request):
	return render_to_response("success.html")
