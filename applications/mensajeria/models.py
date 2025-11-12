from django.db import models
from applications.usuario.models import Usuarios
from applications.sector.models import Nombre_Sector



class Sala(models.Model):
    name = models.OneToOneField(Nombre_Sector, on_delete=models.CASCADE, null=False, to_field='nombre')
    users = models.ManyToManyField(Usuarios, related_name='room_joined', blank=True)

    def __str__(self):
        return str(self.name.nombre)



class Mensaje(models.Model):
    user = models.ForeignKey(Usuarios, on_delete=models.CASCADE, verbose_name='Usuario')
    room = models.ForeignKey(Sala, on_delete=models.CASCADE, verbose_name='Sala')
    message = models.TextField(verbose_name='Mensaje')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Enviado')

    def __str__(self):
        return self.message