from django.contrib import admin
from .models import FichaTecnica, Estado

""" LO QUE SE MUESTRA EN EL /ADMIN """


class FichaTecnicaAdmin(admin.ModelAdmin):
    list_display = (
        "cliente",
        "prototipo",
        "cantidad",
        "fecha_ingreso",
        "fecha_egreso",
        "estado",
        )
    search_fields = ("cliente", "prototipo", "cantidad", "fecha_ingreso", "fecha_egreso",)
    list_filter = ("cliente", "prototipo",)
admin.site.register(FichaTecnica, FichaTecnicaAdmin)



class EstadoAdmin(admin.ModelAdmin):
    list_display = (
        'estado',
        'id',
        )
admin.site.register(Estado, EstadoAdmin)