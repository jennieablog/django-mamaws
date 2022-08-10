# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class Account(AbstractUser):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	# insert fields here

	def __str__(self):
		return self.email

