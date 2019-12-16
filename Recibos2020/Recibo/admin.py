from django.contrib import admin
from .models import Agua
from .models import Luz
from .models import Cuarto

# Register your models here.
class AguaAdmin(admin.ModelAdmin):
    readonly_fields=['Creacion','Actualizacion']


class LuzAdmin(admin.ModelAdmin):
    readonly_fields=['Creacion', 'Actualizacion']


class CuartoAdmin(admin.ModelAdmin):
    readonly_fields=['Creacion', 'Actualizacion']


admin.site.register(Agua, AguaAdmin)
admin.site.register(Luz, LuzAdmin)
admin.site.register(Cuarto, CuartoAdmin)