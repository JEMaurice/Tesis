from django import forms
from .models import FichaTecnica

""" LO QUE SE MUESTRA EN LA WEB, DANDOLE CLASES ATRIBUTOS O PROPIEDADES A LAS ETIQUETAS QUE UTILIZAMOS """


class Formfichatecnica(forms.ModelForm):
    class Meta:
        model = FichaTecnica
        fields = (
            "codigo",
            "cliente",
            "prototipo",
            "cantidad",
            "fecha_ingreso",
            "fecha_egreso",
            "estado",
            "imagen_general",
            "hoja_vida_general",
            "imagen_corte",
            "hoja_vida_corte",
            "imagen_avios",
            "hoja_vida_avios",
            "imagen_estampado",
            "hoja_vida_estampado",
            "imagen_confeccion",
            "hoja_vida_confeccion",
            "hoja_vida_calidad", 
            )
        widgets  = {
            "codigo" : forms.TextInput(attrs={"placeholder" : "Ingrese aqui", "class": "input-general"}),
            "cliente" : forms.Select(attrs={"class": "input-general"}),
            "prototipo" : forms.Select(attrs={"class": "input-general"}),
            "cantidad" : forms.NumberInput(attrs={"class": "input-general", "step": "1"}),
            "estado" : forms.Select(attrs={"class": "input-general"}),

            #https://developer.mozilla.org/es/docs/Learn/Forms/HTML5_input_types
            "fecha_ingreso" : forms.TextInput(attrs={"placeholder" : "dd/mm/aa hh:mm", "type" : "datetime-local", "class": "input-general" }),
            "fecha_egreso" : forms.TextInput(attrs={"placeholder" : "dd/mm/aa hh:mm","type" : "datetime-local", "class": "input-general"}),

            "imagen_general": forms.FileInput(attrs={'class':'form-control'}), 
            "imagen_corte": forms.FileInput(attrs={'class':'form-control'}), 
            "imagen_avios": forms.FileInput(attrs={'class':'form-control'}), 
            "imagen_estampado": forms.FileInput(attrs={'class':'form-control'}), 
            "imagen_confeccion": forms.FileInput(attrs={'class':'form-control'}),

            "hoja_vida_general": forms.Textarea(attrs={'class':'form-control', 'cols': '150', 'rows': '4'}), 
            "hoja_vida_corte": forms.Textarea(attrs={'class':'form-control', 'cols': '150', 'rows': '4'}), 
            "hoja_vida_avios": forms.Textarea(attrs={'class':'form-control', 'cols': '150', 'rows': '4'}), 
            "hoja_vida_estampado": forms.Textarea(attrs={'class':'form-control', 'cols': '150', 'rows': '4'}), 
            "hoja_vida_confeccion": forms.Textarea(attrs={'class':'form-control', 'cols': '150', 'rows': '4'}),
            "hoja_vida_calidad": forms.Textarea(attrs={'class':'form-control', 'cols': '150', 'rows': '4'}),

            }
    def clean_cantidad (self):
        cantidad = self.cleaned_data["cantidad"]
        if cantidad < 0:
            raise forms.ValidationError(" el numero debe ser mayor a 0")
        return cantidad
    

class Formupdatefichatecnica(forms.ModelForm):
    class Meta:
        model = FichaTecnica
        fields = (
            "codigo",
            "cliente",
            "prototipo",
            "cantidad",
            "fecha_ingreso",
            "fecha_egreso",
            "estado",
            "imagen_general",
            "hoja_vida_general",
            "imagen_corte",
            "hoja_vida_corte",
            "imagen_avios",
            "hoja_vida_avios",
            "imagen_estampado",
            "hoja_vida_estampado",
            "imagen_confeccion",
            "hoja_vida_confeccion",
            "hoja_vida_calidad", 
            )
        widgets  = {
            "codigo" : forms.TextInput(attrs={"placeholder" : "Ingrese aqui", "class": "input-general"}),
            "cliente" : forms.Select(attrs={"class": "input-general"}),
            "prototipo" : forms.Select(attrs={"class": "input-general"}),
            "cantidad" : forms.NumberInput(attrs={"class": "input-general", "step": "1"}),
            "estado" : forms.Select(attrs={"class": "input-general"}),

            #https://developer.mozilla.org/es/docs/Learn/Forms/HTML5_input_types
            "fecha_ingreso" : forms.TextInput(attrs={"placeholder" : "dd/mm/aa hh:mm", "type" : "datetime-local" }),
            "fecha_egreso" : forms.TextInput(attrs={"placeholder" : "dd/mm/aa hh:mm","type" : "datetime-local"}),

            "hoja_vida_general": forms.Textarea(attrs={'class':'form-control'}), 
            "hoja_vida_corte": forms.Textarea(attrs={'class':'form-control'}), 
            "hoja_vida_avios": forms.Textarea(attrs={'class':'form-control'}), 
            "hoja_vida_estampado": forms.Textarea(attrs={'class':'form-control'}), 
            "hoja_vida_confeccion": forms.Textarea(attrs={'class':'form-control'}),
            "hoja_vida_calidad": forms.Textarea(attrs={'class':'form-control'}),

            }
    def clean_cantidad (self):
        cantidad = self.cleaned_data["cantidad"]
        if cantidad < 0:
            raise forms.ValidationError(" el numero debe ser mayor a 0")
        return cantidad