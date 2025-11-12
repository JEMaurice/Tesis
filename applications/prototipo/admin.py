from django.contrib import admin
from .models import NombrePrototipo, Prototipo, Piezas, PiezaPrototipo ,Tipo_Pieza

""" LO QUE SE MUESTRA EN EL /ADMIN """


class TipoPiezaAdmin(admin.ModelAdmin):
    list_display = (
        'tipo',
        'id',
        )
admin.site.register(Tipo_Pieza, TipoPiezaAdmin)



class NombrePrototipoAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        )
    search_fields = ("nombre",)
admin.site.register(NombrePrototipo, NombrePrototipoAdmin)



class PiezasAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        )
    search_fields = ("nombre",)
admin.site.register(Piezas, PiezasAdmin)



class PiezaPrototipoAdmin(admin.ModelAdmin):
    list_display = (
        "nombreprototipo",
        "piezas",
        "tipo_pieza",
        "cantidad",
        "ancho",
        "alto",
        "metros",
        )
    search_fields = ("piezas", "cantidad",)
    list_filter = ("piezas", "cantidad",)
admin.site.register(PiezaPrototipo, PiezaPrototipoAdmin)



class ProtAdmin(admin.ModelAdmin):
    list_display = (
        "get_custom_id",
        'nombre',
        'imagen',
        )
    filter_horizontal = ("prototipo_armado",)

    def get_custom_id(self, obj):
        # Generar el valor personalizado para el campo 'id'
        return (f'Prototipo {obj.id}')
    get_custom_id.short_description = 'ID Personalizado'
admin.site.register(Prototipo, ProtAdmin)