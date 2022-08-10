from django.contrib import admin
from .forms import ReservationCreationForm
from .models import Mascot, Service, Performer, Equipment, Reservation, MascotReservation, ServiceReservation, PerformerReservation, EquipmentReservation

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

# Register your models here.
admin.site.register(Mascot)
admin.site.register(Service)
admin.site.register(Performer)
admin.site.register(Equipment)
admin.site.register(Reservation, ReservationAdmin)
