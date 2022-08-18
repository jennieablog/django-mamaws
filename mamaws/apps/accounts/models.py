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
	
	def notification_count(self):
		return Notification.objects.filter(account=self, is_read=False).count()

class Notification(models.Model):
	account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="notifications")
	message = models.CharField(max_length=200)
	url = models.CharField(max_length=200)
	is_read = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.message
