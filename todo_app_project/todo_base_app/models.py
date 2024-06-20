from django.db import models

from accounts.models import User

# Create your models here.

class Todo(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField(max_length=300, null=True, blank=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	is_completed = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


	def __str__(self):
		return self.title

