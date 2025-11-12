from django import forms
from .models import Tipo_Color, Tipo_Insumo, Insumo, TipoUnidad

""" LO QUE SE MUESTRA EN LA WEB, DANDOLE CLASES ATRIBUTOS O PROPIEDADES A LAS ETIQUETAS QUE UTILIZAMOS """


class FormTipounidad(forms.ModelForm):
    class Meta:
        model = TipoUnidad
        fields = (
            "nombre",
            )
        widgets  = {
            "nombre" : forms.TextInput(attrs={"placeholder" : "Ingresar aqui", "class": "input-general"})
            }



class FormTipoinsumo(forms.ModelForm):
    class Meta:
        model = Tipo_Insumo
        fields = (
            "nombre",
            )
        widgets  = {
            "nombre" : forms.TextInput(attrs={"placeholder" : "Ingresar aqui", "class": "input-general"})
            }



class FormTipocolor(forms.ModelForm):
    class Meta:
        model = Tipo_Color
        fields = (
            "nombre",
            )
        widgets  = {
            "nombre" : forms.TextInput(attrs={"placeholder" : "Ingresar aqui", "class": "input-general"})
            }



class FormInsumo(forms.ModelForm):
    class Meta:
        model = Insumo
        fields = (
            "proveedor",
            "tipo_insumo",
            "tipo_color",
            "hoja_vida",
                )
        widgets  = {
            "proveedor" : forms.Select(attrs={"class": "input-general"}),
            "tipo_insumo" : forms.Select(attrs={"class": "input-general"}),
            "tipo_color" : forms.Select(attrs={"class": "input-general"}),
            "hoja_vida" : forms.Textarea(attrs={"class": "input-general"})
            }