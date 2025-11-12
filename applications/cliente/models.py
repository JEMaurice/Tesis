from django.db import models
from ckeditor.fields import RichTextField



class Contacto_cliente(models.Model):
    nombre = models.CharField("Nombre contacto", max_length=50, blank=False)
    telefono = models.CharField("Telefono contacto", max_length=50, blank=False)

    class Meta:
        verbose_name_plural = "Contacto Cliente"

    def __str__(self):
        return self.nombre + ", " + self.telefono



class Cliente(models.Model):
    cuit_o_cuil = models.CharField("CUIT / CUIL", max_length=50, unique=True, blank=False)
    razon_social = models.CharField("Razon social", max_length=50, unique=True, blank=False)
    fantasia = models.CharField("Nombre fantasia", max_length=50)
    mail = models.EmailField("Mail", max_length=128, blank=True)
    direccion = models.CharField("Direccion", max_length=50, blank=True)
    telefono = models.CharField("Telefono", max_length=50, blank=True)
    imagen = models.ImageField('Imagen',upload_to='cliente', blank=True, default='')
    contacto = models.ForeignKey(Contacto_cliente, default= None, on_delete=models.CASCADE)
    hoja_vida = RichTextField(default= "", blank=True)

    class Meta:
        verbose_name_plural = "Clientes"

    def __str__(self):
        return self.cuit_o_cuil + ", " + self.fantasia