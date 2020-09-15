from . import views
from django.urls import path

urlpatterns = [
    path('xxxxxxx', views.index, name='index'),
    path('', views.index, name='index')
]
