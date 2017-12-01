from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm

def register(request):
	return HttpResponse('register')

def login(request):
	return HttpResponse('login')

def logout(request):
	return HttpResponse('logout')



