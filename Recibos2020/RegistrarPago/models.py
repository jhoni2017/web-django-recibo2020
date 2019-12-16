from django.db import models

#importando los modelos Agua, Lus y Cuarto
from Recibo.models import Agua, Luz, Cuarto
#importamos el modulo de tiempo
from datetime import datetime


# Creamos nuestro(s) modelo.

class RegistrarPagoAgua(models.Model):
    Codigo=models.ForeignKey(Agua,verbose_name="Codigo del servicio ", on_delete=models.CASCADE)
    Fecha=models.DateField(default=datetime.today, verbose_name="Fecha del recibo ")
    Monto=models.FloatField(null=True, blank=True, default=None, verbose_name="Monto del recibo")
    Creacion=models.DateTimeField(auto_now=True, verbose_name="Fecha de creacion")
    Actualizacion=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de actualizacion")


    class Meta:
        verbose_name="Registrar pago de agua"
        verbose_name_plural="Registrar pagos de agua"
        ordering=['-Creacion']

    def __str__(self):
        return str(self.Codigo)

class RegistrarPagoLuz(models.Model):
    Codigo=models.ForeignKey(Luz,verbose_name="Codigo del servicio ", on_delete=models.CASCADE)
    Fecha=models.DateField(default=datetime.today, verbose_name="Fecha del recibo ")
    Monto=models.FloatField(null=True, blank=True, default=None, verbose_name="Monto del recibo")
    Creacion=models.DateTimeField(auto_now=True, verbose_name="Fecha de creacion")
    Actualizacion=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de actualizacion")


    class Meta:
        verbose_name="Registrar pago de luz"
        verbose_name_plural="Registrar pagos de luz"
        ordering=['-Creacion']

    def __str__(self):
        return str(self.Codigo)

class RegistrarPagoCuarto(models.Model):
    Codigo=models.ForeignKey(Cuarto,verbose_name="Numero o Codigo del cuarto  ", on_delete=models.CASCADE)
    Fecha=models.DateField(default=datetime.today, verbose_name="Fecha del recibo ")
    Monto=models.FloatField(null=True, blank=True, default=None, verbose_name="Monto del recibo")
    Creacion=models.DateTimeField(auto_now=True, verbose_name="Fecha de creacion")
    Actualizacion=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de actualizacion")


    class Meta:
        verbose_name="Registrar pago de cuarto"
        verbose_name_plural="Registrar pagos de cuarto"
        ordering=['-Creacion']

    def __str__(self):
        return str(self.Codigo)

    

