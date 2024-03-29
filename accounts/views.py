from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def login_user(request):
	# Check to see if logging in
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		# Authenticate
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, "You have been logged in")
			return redirect('ChecklistSeiscomp:create_view')
		else:
			messages.success(request, "There was an error logging in, please try again")
			return redirect('accounts:login')
	else:
		return render(request, 'login.html')
	
def logout_user(request):
	logout(request)
	messages.success(request, "You have been logged out")
	return redirect('login')