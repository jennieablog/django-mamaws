# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class Account(AbstractUser):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	active_purchase_id = models.IntegerField(default=0, blank=False)
	cart_size = models.IntegerField(default=0, blank=False)


	def __str__(self):
		return self.email

	def name(self):
		return self.first_name + ' ' + self.last_name
