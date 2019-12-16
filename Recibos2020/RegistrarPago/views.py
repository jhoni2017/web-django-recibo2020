from django.shortcuts import render, redirect
#importamos el modelo de usuarios
from django.contrib.auth.models import User
#importamos el modelo de Recibo
from Recibo.models import Agua, Luz, Cuarto
# importamos el modelo RegistrarPago
from RegistrarPago.models import RegistrarPagoAgua, RegistrarPagoLuz, RegistrarPagoCuarto
#importando formulario
from.import forms


#registrando las vistas

def registarPago(request):
    #si estamos identificados devolvemos 

    if request.user.is_authenticated:

        if request.user.is_superuser:

            usuarios=User.objects.all()

            
            recibosluz=Luz.objects.all()
            reciboscuarto=Cuarto.objects.all()

            registrosagua=RegistrarPagoAgua.objects.all()
            registrosluz=RegistrarPagoLuz.objects.all()
            registroscuarto=RegistrarPagoCuarto.objects.all()

            registrarform=forms.RegistrarPagoAguaForm()

            
            return render(request, "RegistrarPago/RegistrarPago.html",{'usuarios':usuarios, 'registrarform':registrarform,'registrosagua':registrosagua } )


    
    #en otro caso devolvemos al login

    return redirect('/')
