from django.db import models
from django.utils import timezone

class User(models.Model):
	email = models.EmailField(primary_key=True, unique=True)
	last_login = models.DateTimeField(default=timezone.now)
	REQUIRED_FIELDS = ()
	USERNAME_FIELD = 'email'

	def is_authenticated(self):
		return True