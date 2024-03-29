# apps/pages/urls.py
from django.urls import path

from .views import *

urlpatterns = [
    path('services/', services, name='services'), #form
    path('my_reservations/', my_reservations, name='my_reservations'), #listing
    path('my_reservations/<int:pk>', reservation_details, name='reservation_details'), #show
    path('shop/category=<str:category>', shop, name='shop'), #listing
    path('cart/', cart, name='cart'),
    path('cart/checkout', cart_checkout, name='cart_checkout'),
	path('cart/<int:pk>/delete', delete_purchase, name='delete_purchase'),
    path('my_orders', my_orders, name='my_orders'), #listing
    path('my_orders/<int:pk>', order_details, name='order_details'), #show
    path('notifications/', notifications, name='notifications'),
    path('performer/<int:pk>', performer_details, name='performer_details'), #show
    path('product/<int:pk>', product_details, name='product_details'), #show
]
