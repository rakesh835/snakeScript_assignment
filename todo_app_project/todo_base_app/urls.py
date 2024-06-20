from django.urls import path

from .views import ( home, create_todo, update_todo,
                    delete_todo, complete_todo, undone_todo,
                    search_todo, completed_todos, todo_details

                )



urlpatterns = [
    path('', home, name='home'),
    path('create-todo/', create_todo, name='create_todo'),
    path('update-todo/<int:pk>/', update_todo, name='update_todo'),
    path('delete-todo/<int:pk>/', delete_todo, name='delete_todo'),

    path('todo-details/<int:pk>/', todo_details, name='todo_details'),
    path('complete-todo/<int:pk>/', complete_todo, name='complete_todo'),
    path('undone-todo/<int:pk>/', undone_todo, name='undone_todo'),
    path('search/', search_todo, name='search_todo'),
    path('completed-todos-list/', completed_todos, name='completed_todos_list'),

]