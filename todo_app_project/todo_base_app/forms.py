from django import forms
from django.forms import ModelForm

from .models import Todo



class TodoForm(forms.ModelForm): # to creat new todo or update existing todo this form is used 

	class Meta:
		model = Todo
		fields = ['title', 'description']


