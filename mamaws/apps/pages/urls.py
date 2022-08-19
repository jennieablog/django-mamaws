# apps/pages/urls.py
from django.urls import path
from django.conf.urls import handler404, handler500

from .views import HomePageView, AboutPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
]