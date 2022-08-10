# apps/pages/urls.py
from django.urls import path

from .views import *

urlpatterns = [
    path('services/', services, name='services'), #form
    path('my_reservations/', my_reservations, name='my_reservations'), #listing
    path('my_reservations/<int:pk>', reservation_details, name='reservation_details'), #show
]
