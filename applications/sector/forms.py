from django import forms
from .models import Nombre_Sector

""" LO QUE SE MUESTRA EN LA WEB, DANDOLE CLASES ATRIBUTOS O PROPIEDADES A LAS ETIQUETAS QUE UTILIZAMOS """


class FormNombresector(forms.ModelForm):
    class Meta:
        model= Nombre_Sector
        fields= (
            "nombre",
            )
        widgets = {
            "nombre": forms.TextInput(attrs={"placeholder": "Ingresar aquí","class": "input-general"}),
            }