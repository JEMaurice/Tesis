from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver



class Nombre_Sector(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField("Nombre del sector", unique=True, max_length=20, blank=False)

    class Meta:
        verbose_name_plural = "Nombre del sector"

    def __str__(self):
        return self.nombre



# Función para asignar IDs condicionalmente
@receiver(pre_save, sender=Nombre_Sector)
def assign_custom_id(sender, instance, **kwargs):
    if instance.id is None:
        # Buscar el ID más grande y agregar 1
        max_id = Nombre_Sector.objects.all().aggregate(models.Max('id'))['id__max']
        if max_id is not None:
            instance.id = max_id + 1
        else:
            instance.id = 7  # Si no hay registros, comenzar en 7