from django.contrib import admin
from .forms import ReservationCreationForm
from .models import *

class MascotReservationInLine(admin.TabularInline):
	model = MascotReservation

class ServiceReservationInLine(admin.TabularInline):
	model = ServiceReservation

class PerformerReservationInLine(admin.TabularInline):
	model = PerformerReservation

class EquipmentReservationInLine(admin.TabularInline):
	model = EquipmentReservation

class ReservationAdmin(admin.ModelAdmin):
	inlines = [
		MascotReservationInLine,
		ServiceReservationInLine,
		PerformerReservationInLine,
		EquipmentReservationInLine,
	]

	add_form = ReservationCreationForm

	list_display = [
		'party_name',
		'created_at',
		'account',
		'status',
		'total_cost'
	]

	list_filter = [
		'status',
	]

class ProductPurchaseInLine(admin.TabularInline):
	model = ProductPurchase

class PurchaseAdmin(admin.ModelAdmin):
	inlines = [
		ProductPurchaseInLine,
	]

	list_display = [
		'id',
		'created_at',
		'account',
		'total_cost',
		'status',
	]

	list_filter = [
		'status',
	]

class MascotAdmin(admin.ModelAdmin):
	list_display = [
		'name',
		'description',
		'price',
	]

class ServiceAdmin(admin.ModelAdmin):
	list_display = [
		'name',
		'description',
		'price',
	]

class EquipmentAdmin(admin.ModelAdmin):
	list_display = [
		'name',
		'description',
		'price',
	]

class PerformerAdmin(admin.ModelAdmin):
	list_display = [
		'name',
		'description',
		'price',
	]

class ProductAdmin(admin.ModelAdmin):
	list_display = [
		'name',
		'description',
		'inventory',
		'unit_price',
	]

# Register your models here.
admin.site.register(Mascot, MascotAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Performer, PerformerAdmin)
admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Purchase, PurchaseAdmin)