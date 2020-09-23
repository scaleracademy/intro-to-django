from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='tasks'),
    path('add_task', views.add_task, name='add_task'),
    path('add_task_2', views.add_task_2, name='add_task_2'),
    path('contact', views.contact, name='contact'),
    path('contact_2', views.contact_2, name='contact_2'),
]
