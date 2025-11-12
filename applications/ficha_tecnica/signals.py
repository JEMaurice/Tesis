from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Estado

@receiver(post_migrate)
def create_initial_data(sender, **kwargs):
    if sender.name == 'applications.ficha_tecnica':
        # Verifica si no hay datos en la tabla Estado
        if not Estado.objects.exists():
            # Crea los datos iniciales
            Estado.objects.create(estado='0')
            Estado.objects.create(estado='1')
            Estado.objects.create(estado='2')
            Estado.objects.create(estado='3')
            Estado.objects.create(estado='4')
        else:
            print('Los datos automaticos del estado ya estan creados')