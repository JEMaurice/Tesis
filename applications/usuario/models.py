from django.db import models
from applications.sector.models import Nombre_Sector
from django.contrib.auth.models import AbstractBaseUser
from .managers import CustomUserManager
from django.db.models.signals import pre_save
from django.dispatch import receiver



class Usuarios(AbstractBaseUser):
    username = models.CharField("Nombre de usuario", unique=True, blank=False, max_length=100)
    sector_asignado = models.ManyToManyField(Nombre_Sector, blank=True) 
    dni = models.CharField("DNI", max_length=20, blank=False)
    nombre = models.CharField("Nombre", max_length=40, blank=False)
    apellido = models.CharField("Apellido", max_length=40, blank=False)
    email = models.EmailField("Mail", max_length=128, blank=False)
    direccion = models.CharField("Direccion", max_length=50, blank=False)
    imagen = models.ImageField('Imagen',upload_to='usuario', null=True, blank=True)
    telefono = models.CharField("Telefono", max_length=50, blank=False)
    contacto = models.CharField("Telefono de contacto", max_length=50, blank=False)
    usuario_activo = models.BooleanField(default=True)
    is_staff = models.BooleanField("Es miembro del staff", default=False)
    is_superuser = models.BooleanField("Es superusuario", default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "nombre", "apellido"]

    class Meta:
        verbose_name_plural = "Usuarios"
        
    def __str__(self):
        return f"{self.nombre}, {self.apellido}"

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    def save(self, *args, **kwargs):
        # Guardar el usuario primero
        super(Usuarios, self).save(*args, **kwargs)
        # Luego, asignar los sectores asignados
        for sector in self.sector_asignado.all():
            self.sector_asignado.add(sector)



# Función para asignar IDs condicionalmente
@receiver(pre_save, sender=Usuarios)
def assign_custom_id(sender, instance, **kwargs):
    if instance.id is None:
        # Buscar el ID más grande y agregar 1
        max_id = Usuarios.objects.all().aggregate(models.Max('id'))['id__max']
        if max_id is not None:
            instance.id = max_id + 1
        else:
            instance.id = 3  # Si no hay registros, comenzar en 7