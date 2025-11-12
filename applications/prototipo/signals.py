from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Tipo_Pieza

@receiver(post_migrate)
def create_initial_data(sender, **kwargs):
    if sender.name == 'applications.prototipo':
        # Verifica si no hay datos en la tabla Tipo_Pieza
        if not Tipo_Pieza.objects.exists():
            # Crea los datos iniciales
            Tipo_Pieza.objects.create(tipo='0')
            Tipo_Pieza.objects.create(tipo='1')
            Tipo_Pieza.objects.create(tipo='2')
        else:
            print('Los datos automaticos de prototipo ya estan creados')