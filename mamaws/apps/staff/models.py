import decimal
from datetime import date, datetime, timedelta

from django.conf import settings
from django.core import validators
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

from mamaws.apps.accounts.models import Account

class PerformerApplication(models.Model):
	APPLICATION_STATUS = (
		('PENDING', 'PENDING'),
		('APPROVED', 'APPROVED'),
		('REJECTED', 'REJECTED'),
	)

	full_name = models.CharField(max_length=200)
	email = models.EmailField(max_length=254, verbose_name='Email address')
	phone_number = models.CharField(max_length=200)
	picture = models.ImageField(upload_to='pictures/', null=True, blank=True)
	resume = models.FileField(upload_to='resumes/', null=True, blank=True)
	hash_code = models.CharField(max_length=8)

	created_at = models.DateTimeField(auto_now_add=True)
	processed_at = models.DateTimeField(null=True, blank=True)
	status = models.CharField(max_length=15, blank=False, choices=APPLICATION_STATUS, default='PENDING')

	def __str__(self):
		return self.hash_code + ' - ' + self.full_name
	
	def process(self):
		self.processed_at = timezone.now()
		self.save()
