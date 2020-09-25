from django.urls import path
from . import views

urlpatterns = [
    path('add_task', views.add_task, name='add_task'),
    path('add_tag', views.add_tag, name='add_tag'),
]