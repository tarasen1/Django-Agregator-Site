from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse

def personalCab(request):
	if request.user.is_authenticated():
		return HttpResponse('hello') 
	else:
		return HttpResponse('not hello(')
