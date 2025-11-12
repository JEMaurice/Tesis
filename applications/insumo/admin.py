from django.contrib import admin
from .models import TipoUnidad, Tipo_Insumo, Tipo_Color, Insumo

""" LO QUE SE MUESTRA EN EL /ADMIN """


class TipoUnidadAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        )
    search_fields = ("nombre",)
admin.site.register(TipoUnidad, TipoUnidadAdmin)



class Tipo_InsumoAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        )
    search_fields = ("nombre",)
admin.site.register(Tipo_Insumo, Tipo_InsumoAdmin)



class Tipo_ColorAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        )
    search_fields = ("nombre",)
admin.site.register(Tipo_Color, Tipo_ColorAdmin)



class InsumoAdmin(admin.ModelAdmin):
    list_display = (
        "proveedor",
        "tipo_insumo",
        "tipo_color",
        )
    search_fields = ("proveedor","tipo_insumo","tipo_color",)
    list_filter = ("proveedor","tipo_insumo","tipo_color",)
admin.site.register(Insumo, InsumoAdmin)