from django.db import models
#importamos un modulo para el tiempo y fecha
from datetime import datetime


# Create your models here.

#CLASE AGUA O TABLA AGUA
class Agua(models.Model):
    Codigo=models.CharField(max_length=8, verbose_name="Codigo del Recibo")
    Creacion=models.DateTimeField(auto_now=True, verbose_name="Fecha de Creacion")
    Actualizacion=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Actualizacion")

    class Meta:
        verbose_name="Agua"
        verbose_name_plural="Agua"
        ordering=['-Creacion']

    def __str__(self):
        return self.Codigo


#CLASE LUZ O TABLA LUZ
class Luz(models.Model):
    Codigo=models.CharField(max_length=8, verbose_name="Codigo del Recibo")
    Creacion=models.DateTimeField(auto_now=True, verbose_name="Fecha de Creacion")
    Actualizacion=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Actualizacion")

    class Meta:
        verbose_name="Luz"
        verbose_name_plural="Luz"
        ordering =['-Creacion']

    def __str__(self):
        return self.Codigo



#CLASE CUARTO O TABLA CUARTO
class Cuarto(models.Model):
    Codigo=models.CharField(max_length=8, verbose_name="Numero o Codigo del Cuarto")
    Creacion=models.DateTimeField(auto_now=True, verbose_name="Fecha de Crecion")
    Actualizacion=models.DateTimeField(auto_now_add=True, verbose_name= "fecha de Actualizacion")

    class Meta:
        verbose_name_plural="Cuarto"
        verbose_name_plural="Cuartos"
        ordering=['-Creacion']

    def __str__(self):
        return self.Codigo

