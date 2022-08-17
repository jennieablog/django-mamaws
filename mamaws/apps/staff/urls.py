# apps/pages/urls.py
from django.urls import path

from .views import *

urlpatterns = [
    path('', dashboard, name='dashboard'), # admin dashboard accessible from web

    path('mascots/', mascots_listing, name='mascots_listing'),
    path('mascots/new', mascots_new, name='mascots_new'),
    path('mascots/<int:pk>/edit', mascots_edit, name='mascots_edit'),
    path('mascots/<int:pk>/delete', mascots_delete, name='mascots_delete'),

    path('services/', services_listing, name='services_listing'),
    path('services/new', services_new, name='services_new'),
    path('services/<int:pk>/edit', services_edit, name='services_edit'),
    path('services/<int:pk>/delete', services_delete, name='services_delete'),

    path('equipments/', equipments_listing, name='equipments_listing'),
    path('equipments/new', equipments_new, name='equipments_new'),
    path('equipments/<int:pk>/edit', equipments_edit, name='equipments_edit'),
    path('equipments/<int:pk>/delete', equipments_delete, name='equipments_delete'),

    path('performers/', performers_listing, name='performers_listing'),
    path('performers/new', performers_new, name='performers_new'),
    path('performers/<int:pk>/edit', performers_edit, name='performers_edit'),
    path('performers/<int:pk>/delete', performers_delete, name='performers_delete'),

    path('products/', products_listing, name='products_listing'),
    path('products/new', products_new, name='products_new'),
    path('products/<int:pk>/edit', products_edit, name='products_edit'),
    path('products/<int:pk>/delete', products_delete, name='products_delete'),

    # path('services/', services, name='services'), #form
    # path('my_reservations/', my_reservations, name='my_reservations'), #listing
    # path('my_reservations/<int:pk>', reservation_details, name='reservation_details'), #show
    # path('my_reservations/<int:pk>/pay', payment, name='payment'),
    # path('shop/category=<str:category>', shop, name='shop'), #listing
    # path('cart/', cart, name='cart'),
	# path('cart/<int:pk>/delete', delete_purchase, name='delete_purchase'),
    # path('my_orders', my_orders, name='my_orders'), #listing
    # path('my_orders/<int:pk>', order_details, name='order_details'), #show
]
