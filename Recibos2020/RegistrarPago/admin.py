from django.contrib import admin
from . models import RegistrarPagoAgua, RegistrarPagoLuz, RegistrarPagoCuarto

# Register your models here.
class RegistrarPagoAguaAdmin(admin.ModelAdmin):
    readonly_fields=['Creacion', 'Actualizacion']

class RegistrarPagoLuzAdmin(admin.ModelAdmin):
    readonly_fields=['Creacion', 'Actualizacion']

class RegistrarPagoCuartoAdmin(admin.ModelAdmin):
    readonly_fields=['Creacion', 'Actualizacion']


admin.site.register(RegistrarPagoAgua, RegistrarPagoAguaAdmin)
admin.site.register(RegistrarPagoLuz, RegistrarPagoLuzAdmin)
admin.site.register(RegistrarPagoCuarto, RegistrarPagoCuartoAdmin)