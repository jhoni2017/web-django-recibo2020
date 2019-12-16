from django.db import models
#importando los usuarios 
from django.contrib.auth.models import User
#importando los modelos Agua, Lus y Cuarto
from Recibo.models import Agua, Luz, Cuarto
#importando los modelos de RegistrarPago
from RegistrarPago.models import RegistrarPagoAgua, RegistrarPagoLuz, RegistrarPagoCuarto
#importamos el modulo de tiempo
from datetime import datetime


# Creamos nuestro(s) modelo.

class GenerarPagoAgua(models.Model):
    Usuario= models.ForeignKey(User,on_delete=models.CASCADE, verbose_name="Usuario a pagar")
    Servicio=models.ForeignKey(Agua,verbose_name="Codigo del servicio ", on_delete=models.CASCADE)
    Fecha=models.DateField(default=datetime.today, verbose_name="Fecha del recibo ")
    Monto=models.FloatField(null=True, blank=True, default=None, verbose_name="Monto del recibo")
    MontoUsuario=models.FloatField(null=True, blank=True, default=None, verbose_name="Monto a pagar el usuario")
    Estado=models.BooleanField(default=False, verbose_name="PAGAR (Marca la casilla si va confirmar el pago)")
    Creacion=models.DateTimeField(auto_now=True, verbose_name="Fecha de creacion")
    Actualizacion=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de actualizacion")


    class Meta:
        verbose_name="Generar pago de agua"
        verbose_name_plural="Generar pagos de agua"
        ordering=['-Creacion']

    def __str__(self):
        return str(self.Usuario)

class GenerarPagoLuz(models.Model):
    Usuario= models.ForeignKey(User,on_delete=models.CASCADE, verbose_name="Usuario a pagar")
    Servicio=models.ForeignKey(Luz,verbose_name="Codigo del servicio ", on_delete=models.CASCADE)
    Fecha=models.DateField(default=datetime.today, verbose_name="Fecha del recibo ")
    Monto=models.FloatField(null=True, blank=True, default=None, verbose_name="Monto del recibo")
    MontoUsuario=models.FloatField(null=True, blank=True, default=None, verbose_name="Monto a pagar el usuario")
    Estado=models.BooleanField(default=False, verbose_name="PAGAR (Marca la casilla si va confirmar el pago)")
    Creacion=models.DateTimeField(auto_now=True, verbose_name="Fecha de creacion")
    Actualizacion=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de actualizacion")

    class Meta:
        
        verbose_name="Generar pago de luz"
        verbose_name_plural="Generar pagos de luz"
        ordering=['-Creacion']

    def __str__(self):
        return str(self.Usuario)

class GenerarPagoCuarto(models.Model):
    Usuario= models.ForeignKey(User,on_delete=models.CASCADE, verbose_name="Usuario a pagar")
    Servicio=models.ForeignKey(Cuarto,verbose_name="Numero o Codigo del cuarto ", on_delete=models.CASCADE)
    Fecha=models.DateField(default=datetime.today, verbose_name="Fecha del recibo ")
    Monto=models.FloatField(null=True, blank=True, default=None, verbose_name="Monto del recibo")
    MontoUsuario=models.FloatField(null=True, blank=True, default=None, verbose_name="Monto a pagar el usuario")
    Estado=models.BooleanField(default=False, verbose_name="PAGAR (Marca la casilla si va confirmar el pago)")
    Creacion=models.DateTimeField(auto_now=True, verbose_name="Fecha de creacion")
    Actualizacion=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de actualizacion")
    

    class Meta:
        verbose_name="Generar pago de cuarto"
        verbose_name_plural="Generar pagos de cuarto"
        ordering=['-Creacion']

    def __str__(self):
        return str(self.Usuario)

    
