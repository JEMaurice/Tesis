from django.contrib import admin
from .models import Nombre_Sector

""" LO QUE SE MUESTRA EN EL /ADMIN """


class Nombre_SectorAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "nombre",
        )
    search_fields = ("nombre",)
    list_filter = ("nombre",)
admin.site.register(Nombre_Sector, Nombre_SectorAdmin)