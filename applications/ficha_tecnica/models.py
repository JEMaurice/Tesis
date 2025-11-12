from django.db import models
from ckeditor.fields import RichTextField
from applications.cliente.models import Cliente
from applications.prototipo.models import Prototipo



class Estado(models.Model):
    JOB_CHOICES = (
        ("0", "Activo"),
        ("1", "Finalizado"),
        ("2", "Cancelado"),
        ("3", "En espera"),
        ("4", "Pausado"),
        )

    estado = models.CharField(max_length=1, choices=JOB_CHOICES, unique=True, )

    def __str__(self):
        return self.get_estado_display()



class FichaTecnica(models.Model):
    codigo = models.CharField('Codigo', unique=True, null=False, blank=False, max_length=15)
    cliente = models.ForeignKey(Cliente, default= None, on_delete=models.CASCADE)
    prototipo = models.ForeignKey(Prototipo, default= None, on_delete=models.CASCADE)
    cantidad = models.IntegerField("Cantidad", default= 0, blank=False)
    fecha_ingreso = models.DateTimeField("Fecha Inicio", editable= True, blank= True)
    fecha_egreso = models.DateTimeField("Fecha Entrega", editable= True, blank= True)
    estado =models.ForeignKey(Estado, default= None, on_delete=models.CASCADE)
    imagen_general = models.ImageField('Imagen general',upload_to='ficha_tecnica', null=False, blank=False)
    hoja_vida_general = RichTextField("Observaciones generales", default="", blank=True)
    imagen_corte = models.ImageField('Imagen corte',upload_to='corte', blank=True, default='')
    hoja_vida_corte = RichTextField("Observaciones corte", default="", blank=True)
    imagen_avios = models.ImageField('Imagen avios',upload_to='avios', blank=True, default='')
    hoja_vida_avios = RichTextField("Observaciones avios",default="", blank=True)
    imagen_estampado = models.ImageField('Imagen estampado',upload_to='estampado', blank=True, default='')
    hoja_vida_estampado = RichTextField("Observaciones estampado",default="", blank=True)
    imagen_confeccion = models.ImageField('Imagen confeccion',upload_to='confeccion', blank=True, default='')
    hoja_vida_confeccion = RichTextField("Observaciones confeccion",default="", blank=True)
    hoja_vida_calidad = RichTextField("Observaciones control de calidad",default="", blank=True)

    """A FUNTURO SE PUEDE COLOCAR QUE INSUMOS SE UTILIZO, PARA PODER CONECTAR LOS PROVEEDORES Y SUS INSUMOS,
    POR EL MOMENTO SE ENCUENTRA SEPARADO Y LOS PROVEEDORES SIRVEN COMO AGENDA."""
    
    class Meta:
        verbose_name_plural = "Ficha Tecnica"
        
    def __str__(self):
        return (self.codigo) + ", " + str(self.cliente.fantasia) + ", " + (self.prototipo.nombre  + " " + str(self.prototipo.id))