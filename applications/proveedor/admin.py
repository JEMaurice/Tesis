from django.contrib import admin
from .models import Contacto_proveedores, Proveedores

""" LO QUE SE MUESTRA EN EL /ADMIN """


class ProveedorAdmin(admin.ModelAdmin):
    list_display = (
        "cuit_o_cuil",
        "razon_social",
        "mail",
        )
    search_fields = ("cuit_o_cuil", "razon_social",)
    list_filter = ("mail",)
admin.site.register(Proveedores, ProveedorAdmin)



class Contacto_proveedoresAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "telefono",
        )
    search_fields = ("nombre", "telefono",)
    list_filter = ("nombre",)
admin.site.register(Contacto_proveedores, Contacto_proveedoresAdmin)