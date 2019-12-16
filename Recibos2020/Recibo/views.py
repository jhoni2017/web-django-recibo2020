from django.shortcuts import render, redirect

# Create your views here.
def recibo(request):
    return render (request, "Recibo/Recibo.html")