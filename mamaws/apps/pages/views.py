# apps/pages/views.py
from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

class ContactPageView(TemplateView):
    template_name = 'pages/contact.html'

def error404PageView(request, exception):
    response = render(request, 'pages/404.html', status=404)
    response.status_code = 404
    return response

def error500PageView(request):
    response = render(request,'pages/500.html', status=500)
    response.status_code = 500
    return response
