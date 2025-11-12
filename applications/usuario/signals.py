from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Usuarios

@receiver(post_migrate)
def create_initial_data(sender, **kwargs):
    if sender.name == 'applications.usuario':
        # Verifica si no hay datos en la tabla Nombre_Sector
        if not Usuarios.objects.exists():
            # Crea los datos iniciales
            user = Usuarios(id=1, username='admin', dni='3453453453', nombre='admino', apellido='adminos', email='admins@admins.com', is_superuser=True, is_staff=True)
            user.set_password('admin')
            user.save()

            user2 = Usuarios(id=2, username='admin2', dni='234234234', nombre='admina', apellido='adminas', email='admins2@admins2.com', is_superuser=True, is_staff=True)
            user2.set_password('admin2')
            user2.save()
        else:
            print('Los datos automáticos de Usuario ya están creados')