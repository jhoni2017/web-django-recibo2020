from django.shortcuts import render, redirect

# Creando las vistas.
def generarPago(request):
    if request.user.is_authenticated:
        
        return render(request, "GenerarPago/GenerarPago.html")
    return redirect('/')