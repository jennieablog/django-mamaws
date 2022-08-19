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

    path('reservations/', reservations_listing, name='reservations_listing'),
    path('reservations/<int:pk>/process', reservations_process, name='reservations_process'),

    path('orders/', orders_listing, name='orders_listing'),
    path('orders/<int:pk>/deliver', orders_deliver, name='orders_deliver'),
    path('orders/<int:pk>/fulfill', orders_fulfill, name='orders_fulfill'),

    path('perfomer_application/', performer_application, name='performer_application'),
    path('performer_application_status/', performer_application_status, name='performer_application_status'),
    path('performer_application_listing/', performer_application_listing, name='performer_application_listing'),
    path('performer_application/<int:pk>/', performer_application_details, name='performer_application_details'),

    path('reservations_report/<str:status>/', reservations_report, name='reservations_report'),
    path('sales_report/<str:status>/', sales_report, name='sales_report'),
    path('applications_report/<str:status>/', applications_report, name='applications_report'),
]
