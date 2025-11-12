from django.contrib import admin
from .models import Sala, Mensaje

""" LO QUE SE MUESTRA EN EL /ADMIN """


class MensajeAdmin(admin.ModelAdmin):
    list_display = (
        'user', 
        'room', 
        'message', 
        'timestamp'
        
        )
    list_filter = ('room', 'user')

admin.site.register(Mensaje, MensajeAdmin)
admin.site.register(Sala)