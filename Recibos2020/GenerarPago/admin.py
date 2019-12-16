from django.contrib import admin
from .models import GenerarPagoAgua, GenerarPagoLuz, GenerarPagoCuarto

# Registrando los modelos aqui.
class GenerarPagoAguaAdmin(admin.ModelAdmin):
    readonly_fields=['Creacion', 'Actualizacion']
    list_display=('Usuario','Fecha', 'MontoUsuario','Estado')
    search_fields=('Usuario__username', 'Fecha',)
    

class GenerarPagoLuzAdmin(admin.ModelAdmin):
    readonly_fields=['Creacion', 'Actualizacion']
    list_display=('Usuario','Fecha', 'MontoUsuario','Estado')
    search_fields=('Usuario__username', 'Fecha',)
    

class GenerarPagoCuartoAdmin(admin.ModelAdmin):
    readonly_fields=['Creacion', 'Actualizacion']
    list_display=('Usuario','Fecha', 'MontoUsuario','Estado')
    search_fields=('Usuario__username', 'Fecha',)
    

admin.site.register(GenerarPagoAgua,GenerarPagoAguaAdmin)
admin.site.register(GenerarPagoLuz,GenerarPagoLuzAdmin)
admin.site.register(GenerarPagoCuarto, GenerarPagoCuartoAdmin)