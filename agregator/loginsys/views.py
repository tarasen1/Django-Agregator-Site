from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm

def register(request):
	context = {
		'form'	:	UserCreationForm(),
	}
	if request.method == 'POST':
		newuser_form = UserCreationForm(request.POST)
		if newuser_form.is_valid():
			newuser_form.save()
			newuser = auth.authenticate(username=newuser_form.cleaned_data['username'], password=newuser_form.cleaned_data['password2'])
			auth.login(request, newuser)
			return redirect('/')
		else:
			context = {
				'form'	:	newuser_form
			}
	return render(request, 'loginsys/register.html', context)

def login(request):
	context = {}
	if request.method == 'POST':
		username = request.POST.get('username', '')
		password = request.POST.get('password', '')
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(request, user)
			return redirect('/')
		else:
			context = {
				'login_error'	:	'Incorrect login or password',
			}
			return render(request, 'loginsys/login.html', context)
	else:
		return render(request, 'loginsys/login.html', context)

def logout(request):
	auth.logout(request)
	return redirect('/')



