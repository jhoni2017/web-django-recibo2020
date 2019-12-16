from django.urls import path
from . import views


urlpatterns=[
   path('', views.generarPago, name="generarPago") ,
]