from django.db import models
from ckeditor.fields import RichTextField



class Contacto_proveedores(models.Model):
    nombre = models.CharField("Nombre contacto", max_length=40, blank=False)
    telefono = models.CharField("Telefono contacto", max_length=40, blank=False)

    class Meta:
        verbose_name_plural = "Contacto Proveedores"

    def __str__(self):
        return self.nombre + ", " + self.telefono



class Proveedores(models.Model):
    cuit_o_cuil = models.CharField("CUIT / CUIL", max_length=50, unique=True, blank=False)
    razon_social = models.CharField("Razon social", max_length=50, unique=True, blank=False)
    mail = models.EmailField("Mail", max_length=128, blank=True)
    direccion = models.CharField("Direccion", max_length=50, blank=True)
    telefono = models.CharField("Telefono", max_length=50, blank=True)
    imagen = models.ImageField('Imagen',upload_to='proveedor', blank=True, default='')
    contacto_proveedor = models.ForeignKey(Contacto_proveedores, default= None, on_delete=models.CASCADE)
    hoja_vida = RichTextField(default="", blank=True)
    
    class Meta:
        verbose_name_plural = "Proveedores"

    def __str__(self):
        return str(self.id)+ ", " + self.cuit_o_cuil + ", " + self.razon_social