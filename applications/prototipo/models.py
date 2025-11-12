from django.db import models



class Piezas(models.Model):
    nombre =models.CharField("Nombre de Pieza", max_length=50, blank= False, unique=True)

    class Meta:
        verbose_name_plural = "Nombre de Pieza"

    def __str__(self): 
        return self.nombre



class Tipo_Pieza(models.Model):
    JOB_CHOICES = (
        ("0", "contables"),
        ("1", "cortables"),
        ("2", "medibles"),
        )

    tipo = models.CharField(max_length=1, choices=JOB_CHOICES, unique=True)

    def __str__(self):
        return self.get_tipo_display()



class NombrePrototipo(models.Model):
    nombre =models.CharField("Nombre de Prototipo", max_length=40, blank= False, unique=True)

    class Meta:
        verbose_name_plural = "Nombre de Prototipo"

    def __str__(self): 
        return self.nombre



class PiezaPrototipo(models.Model):
    nombreprototipo =models.ForeignKey(NombrePrototipo, default= None, on_delete=models.CASCADE)
    tipo_pieza = models.ForeignKey(Tipo_Pieza, on_delete=models.CASCADE)
    piezas = models.ForeignKey(Piezas , default= None, on_delete=models.CASCADE)
    cantidad = models.IntegerField("Cantidad", blank=False)
    ancho =models.DecimalField("Ancho", max_digits=3, decimal_places=2,default= 0, blank=True)
    alto =models.DecimalField("Alto", max_digits=3, decimal_places=2,default= 0, blank=True)
    metros =models.DecimalField("Metros", max_digits=3, decimal_places=2,default= 0, blank=True)

    class Meta:
        verbose_name_plural = "Piezas de prototipo con unidad de medida"

    def __str__(self):
        return  str(self.nombreprototipo.nombre) + ", " + self.piezas.nombre + ", " + str(self.cantidad) + ", " + str(self.ancho) + ", " + str(self.alto) + ", " + str(self.metros)



class Prototipo(models.Model):
    nombre =models.CharField("Nombre asignado", max_length=100, blank= False, unique=True)
    prototipo_armado =models.ManyToManyField(PiezaPrototipo)
    imagen =models.ImageField('Imagen',upload_to='prototipo', blank=True, default='')
    
    class Meta:
        verbose_name_plural = "Prototipo"

    def __str__(self): 
        return ("Prototipo " + str(self.id)) + ", " + self.nombre