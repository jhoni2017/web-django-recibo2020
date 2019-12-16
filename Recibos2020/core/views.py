from django.shortcuts import render, redirect

# Creando nuestras vistas
def base(request):
    return render(request, "core/base.html")


