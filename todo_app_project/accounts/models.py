from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


# Custom User manager inherited from BaseUser Manager
class MyUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name=None, password=None):
        """
        Creates and saves a User
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name=None, password=None):
        """
        Creates and saves a superuser 
        """
        user = self.create_user(
        	email,
        	first_name,
            last_name,
            password=password,
        )

        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
	first_name = models.CharField(max_length=150)
	last_name = models.CharField(max_length=150, null=True, blank=True)
	email = models.EmailField(max_length=255, unique=True)
		
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = MyUserManager() # custom user manager defined above

	USERNAME_FIELD = "email" # Here we are using email instead of default username
	REQUIRED_FIELDS = ["first_name"]

	def __str__(self):
	    return self.email

	def full_name(self):
		if self.last_name != None:
			return f'{self.first_name} {self.last_name}'
		return self.first_name

	def has_perm(self, perm, obj=None):
	    "Does the user have a specific permission?"
	    return True

	def has_module_perms(self, app_label):
	    "Does the user have permissions to view the app `app_label`?"
	    return True

	@property
	def is_staff(self):
	    "Is the user a member of staff?"
	    return self.is_admin

