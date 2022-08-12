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

# Register your models here.
admin.site.register(Mascot)
admin.site.register(Service)
admin.site.register(Performer)
admin.site.register(Equipment)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Product)
admin.site.register(Purchase, PurchaseAdmin)