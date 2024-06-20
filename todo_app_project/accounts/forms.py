from django import forms
from django.core.exceptions import ValidationError

from django.forms import ModelForm
from .models import User


# Form to register user 
class UserRegistrationForm(forms.ModelForm):
	password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
	password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

	class Meta:
		model = User # using User model to create user
		fields = ['email', 'first_name', 'last_name', 'password1', 'password2']


	#field level validation to check if both passwords are same
	def clean_password2(self):
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')
		if password1 and password2 and password1 != password2:
		    raise ValidationError("Passwords don't match!")
		return password1