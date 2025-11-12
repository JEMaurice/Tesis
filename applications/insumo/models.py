from django.db import models
from ckeditor.fields import RichTextField
from applications.proveedor.models import Proveedores



""" ver el tipo de unidad no lo uso en ningun lado """
class TipoUnidad(models.Model):
    nombre = models.CharField("Tipo de unidad a medir", unique=True,blank=False, max_length=40)

    class Meta:
        verbose_name_plural = "Unidad de medicion"

    def __str__(self):
        return self.nombre



class Tipo_Insumo(models.Model):
    nombre =models.CharField("Nombre de insumo", unique=True, blank=False, max_length=40)

    class Meta:
        verbose_name_plural = "Tipo de insumo"
        
    def __str__(self): 
        return self.nombre



class Tipo_Color(models.Model):
    nombre =models.CharField("Nombre del color", unique=True, blank=False, max_length=40)

    class Meta:
        verbose_name_plural = "Tipo de color"
        
    def __str__(self):
        return self.nombre



class Insumo(models.Model):
    proveedor = models.ForeignKey(Proveedores, default= None, on_delete=models.CASCADE)
    tipo_insumo = models.ForeignKey(Tipo_Insumo , default= None, on_delete=models.CASCADE)
    tipo_color = models.ForeignKey(Tipo_Color , default= None, on_delete=models.CASCADE)
    hoja_vida = RichTextField(default="", blank=True)

    class Meta:
        verbose_name_plural = "Insumos"
        
    def __str__(self):
        return self.proveedor.razon_social + ", " + str(self.tipo_insumo) + ", " + str(self.tipo_color)