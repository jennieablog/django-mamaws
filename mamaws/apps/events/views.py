from datetime import date, datetime, timedelta
import requests

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.forms.models import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from .forms import ReservationCreationForm
from .models import *
import json

@login_required
def services(request):
	if request.method == "POST":
		form = ReservationCreationForm(request.POST)
		if form.is_valid():
			reservation = form.save(commit=False)
			reservation.account = request.user
			reservation.status = 'PENDING'
			reservation.save()

			keys = request.POST.keys()
			
			max_range = Mascot.objects.count() + 1
			for x in range(1, max_range):
				key = 'mascot'+str(x)
				if key in keys:
					mascot_id = request.POST[key]
					mascot = get_object_or_404(Mascot, id=mascot_id)
					MascotReservation.objects.create(mascot=mascot, reservation=reservation, price=mascot.price)
			
			max_range = Service.objects.count() + 1
			for x in range(1, max_range):
				key = 'service'+str(x)
				if key in keys:
					service_id = request.POST[key]
					service = get_object_or_404(Service, id=service_id)
					ServiceReservation.objects.create(service=service, reservation=reservation, price=service.price)
			
			max_range = Equipment.objects.count() + 1
			for x in range(1, max_range):
				key = 'equipment'+str(x)
				if key in keys:
					equipment_id = request.POST[key]
					equipment = get_object_or_404(Equipment, id=equipment_id)
					EquipmentReservation.objects.create(equipment=equipment, reservation=reservation, price=equipment.price)
			
			max_range = Performer.objects.count() + 1
			for x in range(1, max_range):
				key = 'performer'+str(x)
				if key in keys:
					performer_id = request.POST[key]
					performer = get_object_or_404(Performer, id=performer_id)
					PerformerReservation.objects.create(performer=performer, reservation=reservation, price=performer.price)

			reservation.updateTotalCost()
			reservation.save()
			return redirect('my_reservations')
		else:
			messages.error(request, _('There was an error:'+str(form.errors)))
	
	context = {
		"form": ReservationCreationForm(),
		"mascots": Mascot.objects.all(),
		"services": Service.objects.all(),
		"performers": Performer.objects.all(),
		"equipments": Equipment.objects.all(),
	}
	return render(request, 'events/form.html', context)

@login_required
def my_reservations(request):
	context = {
		"reservations": Reservation.objects.filter(account=request.user)
	}
	return render(request, 'events/listing.html', context)

@login_required
def reservation_details(request, pk):
	reservation = get_object_or_404(Reservation, id=pk)
	context = {
		"reservation": reservation,
	}
	return render(request, 'events/details.html', context)

@login_required
def payment(request, pk):
	reservation = get_object_or_404(Reservation, id=pk)
	context = {
		"reservation": reservation,
	}
	return render(request, 'events/payment.html', context)

@login_required
def shop(request):
	if request.method == "POST":
		product_id = request.POST['product']
		quantity = request.POST['quantity']
		product = get_object_or_404(Product, id=product_id)
		purchase = get_object_or_404(Purchase, id=request.user.active_purchase_id)
		ProductPurchase.objects.create(
			product=product,
			purchase=purchase,
			quantity=quantity,
			unit_price=product.unit_price,
		)

		product.inventory = product.inventory - int(quantity)
		product.save()

		purchase.updateTotalCost()
		purchase.save()

		request.user.cart_size += 1
		request.user.save()

		messages.success(request, _('Product successfully added to your cart!'))
		return redirect('shop')
	else:
		products = Product.objects.all()
		context = {
			"products": products,
		}
		return render(request, 'shop/shop.html', context)

@login_required
def cart(request):
	purchase = get_object_or_404(Purchase, id=request.user.active_purchase_id)
	products = ProductPurchase.objects.filter(purchase=purchase)
	context = {
		"products": products,
		"order": purchase,
	}

	return render(request, 'shop/cart.html', context)

@login_required
def delete_purchase(request, pk):
	product_purchase = get_object_or_404(ProductPurchase, id=pk)
	purchase = product_purchase.purchase
	if product_purchase.purchase.account == request.user:
		product_purchase.delete()
		purchase.updateTotalCost()
		purchase.save()
		request.user.cart_size -= 1
		request.user.save()
		messages.success(request, _('Product successfully removed from your cart!'))
	return redirect('cart')

@login_required
def my_orders(request):
	context = {
		"orders": Purchase.objects.filter(account=request.user, total_cost__gt=0),
	}
	return render(request, 'shop/listing.html', context)

@login_required
def order_details(request, pk):
	purchase = get_object_or_404(Purchase, id=pk)
	context = {
		"order": purchase,
		"products": purchase.products.all(),
	}
	return render(request, 'shop/details.html', context)
