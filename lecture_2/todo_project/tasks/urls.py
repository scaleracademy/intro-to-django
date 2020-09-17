from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', views.index_page),
    path('about', TemplateView.as_view(template_name='about.html')),
    path('blog', TemplateView.as_view(template_name='blog.html')),
]
