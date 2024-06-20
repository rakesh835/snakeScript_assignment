from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import UserRegistrationForm
from accounts.models import User

# Create your views here.


def register_user(request): # function to create user account
	if request.user.is_authenticated:
		messages.warning(request, 'Your are already registerd.')
		return redirect('home')

	form = UserRegistrationForm(request.POST or None)

	if request.method == 'POST':
		if form.is_valid():
			email = form.cleaned_data.get('email')
			first_name = form.cleaned_data.get('first_name')
			last_name = form.cleaned_data.get('last_name')
			password = form.cleaned_data.get('password1')
			user = User.objects.create_user(email=email, first_name=first_name, last_name=last_name, password=password)

			messages.success(request, 'Your are registerd successfully.')
			return redirect('home')
		else:
			messages.warning(request, 'There is error in fields.')

	context = {
			'form': form
	}

	return render(request, 'accounts/register_user.html', context)



def login_user(request):
	if request.user.is_authenticated:
		messages.warning(request, 'Your are already logged in.')
		return redirect('home')


	if request.method == 'POST':
		email = request.POST.get('email')
		password = request.POST.get('password')
		user = authenticate(request, email=email, password=password)
	
		if user is not None:
			login(request, user) # user session is created
			messages.success(request, 'Your are logged in successfully.')
			return redirect('home')
		else:
			messages.success(request, "Email or password is not valid.")
			return redirect('login_user')
	else:
		 return render(request, 'accounts/login_user.html')



# unauthorized user can't user logout functionality throug urls
@login_required
def logout_user(request):
	
	logout(request)
	messages.success(request, "You are logged out successfully.")

	return redirect('home')