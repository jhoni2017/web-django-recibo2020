from django.urls import path
from . import views

urlpatterns=[
    path('', views.registarPago, name="registrarPago"),
]