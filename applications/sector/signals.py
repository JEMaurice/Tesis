from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Nombre_Sector

@receiver(post_migrate)
def create_initial_data(sender, **kwargs):
    if sender.name == 'applications.sector':
        # Verifica si no hay datos en la tabla Nombre_Sector
        if not Nombre_Sector.objects.exists():
            # Crea los datos iniciales
            Nombre_Sector.objects.create(id=1, nombre='Administración')
            Nombre_Sector.objects.create(id=2, nombre='Corte')
            Nombre_Sector.objects.create(id=3, nombre='Avios')
            Nombre_Sector.objects.create(id=4, nombre='Estampado')
            Nombre_Sector.objects.create(id=5, nombre='Confección')
            Nombre_Sector.objects.create(id=6, nombre='Control de calidad')
        else:
            print('Los datos automáticos de Nombre_Sector ya están creados')