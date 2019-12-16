from django.urls import path
from . import views

urlpatterns=[
    path('',views.login, name="login" ),
    path('salir',views.salir, name="salir" ),
    path('home',views.home, name="home" ),
]