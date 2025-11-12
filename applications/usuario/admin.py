from django.contrib import admin
from .models import Usuarios

""" LO QUE SE MUESTRA EN EL /ADMIN """


class UsuariosAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "nombre",
        "username",
        "dni",
        "nombre",
        "apellido",
        "email",
        "nombre_completo",
        )
    #combina y crea columna nueva en este caso combinamos nombre y apellido
    #con el nombre de colunma nombre completo
    def nombre_completo(self, obj):
        return obj.nombre + " " + obj.apellido
    filter_horizontal = ("sector_asignado",)
    #buscador en heather horizontal
    search_fields = ("username","nombre", "apellido",)
    #filtrado especifico al lateral derecho
    list_filter = ("username","nombre", "apellido",)
admin.site.register(Usuarios, UsuariosAdmin)