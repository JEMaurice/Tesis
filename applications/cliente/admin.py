from django.contrib import admin
from .models import Cliente, Contacto_cliente

""" LO QUE SE MUESTRA EN EL /ADMIN """


class ClienteAdmin(admin.ModelAdmin):
    list_display = (
        "cuit_o_cuil",
        "razon_social",
        "fantasia",
        "mail",
        "direccion",
        "telefono",
        "imagen",
        )
    search_fields = ("cuit_o_cuil", "razon_social", "fantasia", "mail", "direccion", "telefono", "imagen",)
    list_filter = ("cuit_o_cuil", "razon_social", "fantasia",)
admin.site.register(Cliente, ClienteAdmin)



class Contacto_clienteAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "telefono",
        )
    search_fields = ("nombre", "telefono",)
    list_filter = ("nombre",)
admin.site.register(Contacto_cliente, Contacto_clienteAdmin)