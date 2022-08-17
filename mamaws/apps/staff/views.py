from datetime import date, datetime, timedelta
import requests

from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required, user_passes_test
from django.forms.models import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from mamaws.apps.accounts.models import *
from mamaws.apps.events.models import *

from .forms import *
from .models import *

import json

@staff_member_required
def dashboard(request):
	return render(request, 'staff/dashboard.html')

@staff_member_required
def mascots_listing(request):
	context = {
		"mascots": Mascot.objects.all(),
	}

	return render(request, 'staff/mascots/listing.html', context)

@staff_member_required
def mascots_new(request):
	if request.method == 'POST':
		form = MascotForm(request.POST, request.FILES)
		if form.is_valid():
			mascot = form.save()
			messages.success(request, _('New Mascot successfully added!'))
			return redirect('mascots_listing')
		else:
			messages.error(request, _('There was an error:'+str(form.errors)))
	return render(request, 'staff/mascots/new.html')

@staff_member_required
def mascots_edit(request, pk):
	mascot = get_object_or_404(Mascot, id=pk)

	if request.method == 'POST':
		form = MascotForm(request.POST, request.FILES, instance=mascot)
		if form.is_valid():
			mascot = form.save()
			messages.success(request, _('Mascot successfully updated!'))
			return redirect('mascots_listing')
		else:
			messages.error(request, _('There was an error:'+str(form.errors)))
	return render(request, 'staff/mascots/edit.html', { "mascot": mascot })

@staff_member_required
def mascots_delete(request, pk):
	mascot = get_object_or_404(Mascot, id=pk)
	mascot.delete()
	messages.success(request, _('Mascot successfully removed!'))
	return redirect('mascots_listing')

@staff_member_required
def services_listing(request):
	context = {
		"services": Service.objects.all(),
	}

	return render(request, 'staff/services/listing.html', context)

@staff_member_required
def services_new(request):
	if request.method == 'POST':
		form = ServiceForm(request.POST, request.FILES)
		if form.is_valid():
			service = form.save()
			messages.success(request, _('New Service successfully added!'))
			return redirect('services_listing')
		else:
			messages.error(request, _('There was an error:'+str(form.errors)))
	return render(request, 'staff/services/new.html')

@staff_member_required
def services_edit(request, pk):
	service = get_object_or_404(Service, id=pk)

	if request.method == 'POST':
		form = ServiceForm(request.POST, request.FILES, instance=service)
		if form.is_valid():
			service = form.save()
			messages.success(request, _('Service successfully updated!'))
			return redirect('services_listing')
		else:
			messages.error(request, _('There was an error:'+str(form.errors)))
	return render(request, 'staff/services/edit.html', { "service": service })

@staff_member_required
def services_delete(request, pk):
	service = get_object_or_404(Service, id=pk)
	service.delete()
	messages.success(request, _('Service successfully removed!'))
	return redirect('services_listing')

@staff_member_required
def equipments_listing(request):
	context = {
		"equipments": Equipment.objects.all(),
	}

	return render(request, 'staff/equipments/listing.html', context)

@staff_member_required
def equipments_new(request):
	if request.method == 'POST':
		form = EquipmentForm(request.POST, request.FILES)
		if form.is_valid():
			equipment = form.save()
			messages.success(request, _('New Equipment successfully added!'))
			return redirect('equipments_listing')
		else:
			messages.error(request, _('There was an error:'+str(form.errors)))
	return render(request, 'staff/equipments/new.html')

@staff_member_required
def equipments_edit(request, pk):
	equipment = get_object_or_404(Equipment, id=pk)

	if request.method == 'POST':
		form = EquipmentForm(request.POST, request.FILES, instance=equipment)
		if form.is_valid():
			equipment = form.save()
			messages.success(request, _('Equipment successfully updated!'))
			return redirect('equipments_listing')
		else:
			messages.error(request, _('There was an error:'+str(form.errors)))
	return render(request, 'staff/equipments/edit.html', { "equipment": equipment })

@staff_member_required
def equipments_delete(request, pk):
	equipment = get_object_or_404(Equipment, id=pk)
	equipment.delete()
	messages.success(request, _('Equipment successfully removed!'))
	return redirect('equipments_listing')

@staff_member_required
def performers_listing(request):
	context = {
		"performers": Performer.objects.all(),
	}

	return render(request, 'staff/performers/listing.html', context)

@staff_member_required
def performers_new(request):
	if request.method == 'POST':
		form = PerformerForm(request.POST, request.FILES)
		if form.is_valid():
			performer = form.save()
			messages.success(request, _('New Performer successfully added!'))
			return redirect('performers_listing')
		else:
			messages.error(request, _('There was an error:'+str(form.errors)))
	return render(request, 'staff/performers/new.html')

@staff_member_required
def performers_edit(request, pk):
	performer = get_object_or_404(Performer, id=pk)

	if request.method == 'POST':
		form = PerformerForm(request.POST, request.FILES, instance=performer)
		if form.is_valid():
			performer = form.save()
			messages.success(request, _('Performer successfully updated!'))
			return redirect('performers_listing')
		else:
			messages.error(request, _('There was an error:'+str(form.errors)))
	return render(request, 'staff/performers/edit.html', { "performer": performer })

@staff_member_required
def performers_delete(request, pk):
	performer = get_object_or_404(Performer, id=pk)
	performer.delete()
	messages.success(request, _('Performer successfully removed!'))
	return redirect('performers_listing')

@staff_member_required
def products_listing(request):
	context = {
		"products": Product.objects.all(),
	}

	return render(request, 'staff/products/listing.html', context)

@staff_member_required
def products_new(request):
	if request.method == 'POST':
		form = ProductForm(request.POST, request.FILES)
		if form.is_valid():
			product = form.save()
			messages.success(request, _('New Product successfully added!'))
			return redirect('products_listing')
		else:
			messages.error(request, _('There was an error:'+str(form.errors)))
	return render(request, 'staff/products/new.html')

@staff_member_required
def products_edit(request, pk):
	product = get_object_or_404(Product, id=pk)

	if request.method == 'POST':
		form = ProductForm(request.POST, request.FILES, instance=product)
		if form.is_valid():
			product = form.save()
			messages.success(request, _('Product successfully updated!'))
			return redirect('products_listing')
		else:
			messages.error(request, _('There was an error:'+str(form.errors)))
	return render(request, 'staff/products/edit.html', { "product": product })

@staff_member_required
def products_delete(request, pk):
	product = get_object_or_404(Product, id=pk)
	product.delete()
	messages.success(request, _('Product successfully removed!'))
	return redirect('products_listing')

