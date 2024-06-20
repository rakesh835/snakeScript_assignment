from django.contrib import admin

from .models import Todo

# Register your models here.



class TodoAdmin(admin.ModelAdmin): # Custom admin interface
	list_display = ['title', 'user', 'is_completed', 'updated_at']
	list_filter = ['user', 'is_completed']
	search_fields = ['title']

admin.site.register(Todo, TodoAdmin)