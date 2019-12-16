from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from.forms import LoginForm
from django.contrib.auth.models import User

from GenerarPago.models import GenerarPagoAgua,GenerarPagoLuz,GenerarPagoCuarto

# Create your views here.

def home(request):
    #si estamos identificados 
    if request.user.is_authenticated:


        if request.user.is_staff:
            gpa=GenerarPagoAgua.objects.filter(Usuario=User.objects.get(id=request.user.id))
            gpl=GenerarPagoLuz.objects.filter(Usuario=User.objects.get(id=request.user.id))
            gpc=GenerarPagoCuarto.objects.filter(Usuario=User.objects.get(id=request.user.id))

            return render(request, "login/home.html",{'gpa':gpa, 'gpl':gpl, 'gpc':gpc})

    return redirect('/')




def login(request):
    form=LoginForm()

    if request.method=='POST':
        form=LoginForm(data=request.POST)
        
        if form.is_valid():
            
            username=form.cleaned_data['usuario']
            password=form.cleaned_data['contraseña']

            user=authenticate(username=username, password=password)

            if user is not None:
                do_login(request,user)
                return redirect('home')
    
    return render(request,"login/login.html", {'form':form})


def salir(request):
    #finalizamos la sesion
    do_logout(request)
    #redireccionamos al login
    return redirect('/')
