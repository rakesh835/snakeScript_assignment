from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator

from .models import Todo
from .forms import TodoForm

# Create your views here.


def home(request): # Home page of todo web app

	# we will display only authenticated user's todos
	if request.user.is_authenticated:
		todo_list = Todo.objects.filter(user=request.user, is_completed=False).order_by('-updated_at')
		
		paginator = Paginator(todo_list, 2) # paginator object to display certain todo tasks per page, here 2 tasks per page
		
		page_number = request.GET.get("page", 1)
		todo_list = paginator.get_page(page_number)
	else:
		todo_list = None
		paginator = None

	context = {
			'todo_list': todo_list,
			'paginator': paginator,
	}

	return render(request, 'todo_base_app/home.html', context)


@login_required
def create_todo(request): # create new todo
	todo_form = TodoForm(request.POST or None)

	if request.method == 'POST':
		if todo_form.is_valid:
			todo_task = todo_form.save(commit=False)
			todo_task.user = request.user # authenticated user must be assigned to newly created todo
			todo_task.save()

			messages.success(request, "Todo task created successfully.")
			return redirect('home')
		else:
			messages.success(request, "Error in fields.")

	context = {
			'todo_form': todo_form,
	}

	return render(request, 'todo_base_app/create_todo.html', context)



@login_required
def update_todo(request, pk): 

	# to handle exception if todo doesn't exists
	try:
		todo_task = Todo.objects.get(id=pk, user=request.user)
	except Exception as e: 
		messages.error(request, "Task does not exist.")
		return redirect('home')

	# if todo is completed we don't need to update that todo
	if todo_task.is_completed: 
		messages.warning(request, "You can't update completed todo.")
		return redirect('home')

	if request.method == 'POST':
		todo_form = TodoForm(request.POST or None, instance=todo_task) # current instance is todo we got using pk
		if todo_form.is_valid():
			todo_form.save()
			messages.success(request, "Task updated successfully.")
			return redirect('home')
		else:
			messages.success(request, "Error in fields.")
	else:
		todo_form = TodoForm(instance=todo_task)

	context = {
			'todo_form': todo_form,
			'pk': pk,
	}

	return render(request, 'todo_base_app/update_todo.html', context)



@login_required
def delete_todo(request, pk):
	# to handle exception if todo doesn't exists
	try:
		todo_task = Todo.objects.get(id=pk, user=request.user)
	except:
		messages.error(request, "Todo doesn't exist.")
		return redirect('home')

	if todo_task.is_completed:
		todo_task.delete()	
		messages.success(request, "Task deleted successfully.")
		return redirect('completed_todos_list')
	else:
		todo_task.delete()
		messages.success(request, "Task deleted successfully.")
		return redirect('home')


@login_required
def todo_details(request, pk):
	# to handle exception if todo doesn't exists
	try:
		todo_task = Todo.objects.get(id=pk, user=request.user)
	except:
		messages.error(request, "Todo doesn't exist.")
		return redirect('home')
	
	context = {
			'todo_task': todo_task,
	}

	return render(request, 'todo_base_app/todo_detail.html', context)



@login_required
def complete_todo(request, pk): # To mark a todo as 'completed'

	# to handle exception if todo doesn't exists
	try:
		todo_task = Todo.objects.get(id=pk, user=request.user)
	except:
		messages.error(request, "Todo doesn't exist.")
		return redirect('home')

	if todo_task.is_completed == True:
		messages.error(request, "Task is already marked as 'completed'.")
	else:
		todo_task.is_completed = True
		todo_task.save()
		messages.success(request, "Task is marked as 'completed'.")

	return redirect('home')



@login_required
def undone_todo(request, pk): # To mark a todo as 'undone'

	# to handle exception if todo doesn't exists
	try:
		todo_task = Todo.objects.get(id=pk, user=request.user)
	except:
		messages.error(request, "Todo doesn't exist.")
		return redirect('home')

	if todo_task.is_completed == False:
		messages.error(request, "Task is already marked as 'undone'.")
	else:
		todo_task.is_completed = False
		todo_task.save()
		messages.success(request, "Task is marked as 'undone'.")

	return redirect('home')



def search_todo(request):
	# unauthorized user is not allowed to search
	# because we display only those todos associated with current authenticated user
	if not request.user.is_authenticated:
		messages.error(request, "To search you need to login.")
		return redirect('home')

	if request.method == 'GET':
		query = request.GET.get('query')
		if query:
			todo_list = Todo.objects.filter(Q(title__icontains=query) | Q(description__icontains=query), user=request.user).order_by('-updated_at')

			paginator = Paginator(todo_list, 2) # to display certain todos per page i.e 2 todos per page
		
			page_number = request.GET.get("page", 1)
			todo_list = paginator.get_page(page_number)
		
		else:
			todo_list = None
			paginator = None
			query = ''

	context = {
			'todo_list': todo_list,
			'paginator': paginator,
			'query': query,

	}

	return render(request, 'todo_base_app/search.html', context)



@login_required
def completed_todos(request): # separate list of completed todos.

	todo_list = Todo.objects.filter(user=request.user, is_completed=True).order_by('-updated_at')

	paginator = Paginator(todo_list, 2) # to display certain todos per page i.e 2 todos per page
		
	page_number = request.GET.get("page", 1)
	todo_list = paginator.get_page(page_number)

	context = {
			'todo_list': todo_list,
			'paginator': paginator,
	}

	return render(request, 'todo_base_app/completed_todos.html', context)