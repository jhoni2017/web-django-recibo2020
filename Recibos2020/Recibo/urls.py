from django.urls import path
from . import views

urlpatterns=[
   path('', views.recibo, name="recibo" ),
]