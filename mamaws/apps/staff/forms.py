from django import forms
from .models import *
from mamaws.apps.accounts.models import *
from mamaws.apps.events.models import *

class MascotForm(forms.ModelForm):
	class Meta:
		model = Mascot
		fields = ('name', 'description', 'picture','price',)

class ServiceForm(forms.ModelForm):
	class Meta:
		model = Service
		fields = ('name', 'description', 'picture','price',)

class PerformerForm(forms.ModelForm):
	class Meta:
		model = Performer
		fields = ('name', 'description', 'picture','price',)

class EquipmentForm(forms.ModelForm):
	class Meta:
		model = Equipment
		fields = ('name', 'description', 'picture','price',)

class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = ('name', 'description', 'picture','unit_price','inventory','category',)

class PerformerApplicationForm(forms.ModelForm):
	class Meta:
		model = PerformerApplication
		fields = ('full_name', 'email', 'phone_number', 'picture', 'resume',)
