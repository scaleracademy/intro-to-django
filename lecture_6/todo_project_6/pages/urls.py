from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='pages/home.html'), name='home'),
    path('about', TemplateView.as_view(template_name='pages/about.html'), name='about'),
    path('contact', views.contact, name='contact'),
    path('dashboard', views.dashboard, name='dashboard'),
]
