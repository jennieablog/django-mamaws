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

class Mascot(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField(blank=True, null=True)
	picture = models.ImageField(upload_to='pictures/', null=True, blank=True)
	price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

	def __str__(self):
		return self.name

class Service(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField(blank=True, null=True)
	picture = models.ImageField(upload_to='pictures/', null=True, blank=True)
	price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

	def __str__(self):
		return self.name

class Performer(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField(blank=True, null=True)
	picture = models.ImageField(upload_to='pictures/', null=True, blank=True)
	price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

	def __str__(self):
		return self.name

class Equipment(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField(blank=True, null=True)
	picture = models.ImageField(upload_to='pictures/', null=True, blank=True)
	price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

	def __str__(self):
		return self.name

class Reservation(models.Model):
	RESERVATION_STATUS = (
		('PENDING', 'PENDING'),
		('APPROVED', 'APPROVED'),
		('DENIED', 'DENIED'),
	)

	account = models.ForeignKey(Account, on_delete=models.CASCADE)
	status = models.CharField(max_length=15, blank=False, choices=RESERVATION_STATUS)

	party_name = models.CharField(max_length=200)
	party_address = models.CharField(max_length=200)
	party_size = models.IntegerField(default=0, blank=False)
	party_date = models.DateField(blank=False)
	party_start_time = models.TimeField(blank=False)
	party_end_time = models.TimeField(blank=False)

	phone_number = models.CharField(max_length=20, blank=False)
	notes = models.TextField(blank=True, null=True)
	
	# mascots, services, performer, equipment
	total_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.party_name
	
	def updateTotalCost(self):
		total = 0

		for mascot in self.mascots.all():
			total += mascot.price
		for service in self.services.all():
			total += service.price
		for performer in self.performers.all():
			total += performer.price
		for equipment in self.equipments.all():
			total += equipment.price
		
		self.total_cost = total

class MascotReservation(models.Model):
	mascot = models.ForeignKey(Mascot, on_delete=models.CASCADE)
	reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, related_name="mascots")
	price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

	class Meta:
		unique_together = ('mascot', 'reservation',)

	def __str__(self):
		return self.reservation.party_name + ' - ' + self.mascot.name + ' Reservation'

class ServiceReservation(models.Model):
	service = models.ForeignKey(Service, on_delete=models.CASCADE)
	reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, related_name="services")
	price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

	class Meta:
		unique_together = ('service', 'reservation',)

	def __str__(self):
		return self.reservation.party_name + ' - ' + self.service.name + ' Reservation'

class PerformerReservation(models.Model):
	performer = models.ForeignKey(Performer, on_delete=models.CASCADE)
	reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, related_name="performers")
	price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

	class Meta:
		unique_together = ('performer', 'reservation',)

	def __str__(self):
		return self.reservation.party_name + ' - ' + self.performer.name + ' Reservation'

class EquipmentReservation(models.Model):
	equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
	reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, related_name="equipments")
	price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

	class Meta:
		unique_together = ('equipment', 'reservation',)

	def __str__(self):
		return self.reservation.party_name + ' - ' + self.equipment.name + ' Reservation'

class Product(models.Model):
	CATEGORY = (
		('ballo', 'Balloons'),
		('banne', 'Banners'),
		('gRBox', 'Gender Reveal Box'),
		('gWrap', 'Gift Wrapper'),
		('tACha', 'Table and Chairs'),
		('dCurt', 'Decorative Curtains'),
		('cTopp', 'Cake Toppers'),
	)

	name = models.CharField(max_length=200)
	description = models.TextField(blank=True, null=True)
	picture = models.ImageField(upload_to='pictures/', null=True, blank=True)
	unit_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
	inventory = models.IntegerField(default=0, blank=False)

	category = models.CharField(max_length=5, blank=False, choices=CATEGORY)

	def __str__(self):
		return self.name

class Purchase(models.Model):
	PURCHASE_STATUS = (
		('TO PAY', 'TO PAY'),
		('PAID', 'PAID'),
	)

	account = models.ForeignKey(Account, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	total_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

	status = models.CharField(max_length=15, blank=False, choices=PURCHASE_STATUS, default='TO PAY')

	def __str__(self):
		return self.account.first_name + ' ' + self.account.last_name + ' ' + str(self.created_at)

	def updateTotalCost(self):
		total = 0
		
		for product in self.products.all():
			total += product.line_total()
		
		self.total_cost = total
	
	def total_quantity(self):
		total = 0
		
		for product in self.products.all():
			total += product.quantity
		
		return total

class ProductPurchase(models.Model):
	purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE, related_name="products")
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	quantity = models.IntegerField(default=0, blank=False)
	unit_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

	def __str__(self):
		return self.product.name + ' (' + str(self.quantity) + ' pc) - PO#' + str(self.purchase.id)
	
	def line_total(self):
		return self.quantity * self.unit_price
