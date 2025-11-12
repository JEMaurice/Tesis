from django import forms
from applications.usuario.models import Usuarios

""" LO QUE SE MUESTRA EN LA WEB, DANDOLE CLASES ATRIBUTOS O PROPIEDADES A LAS ETIQUETAS QUE UTILIZAMOS """


class FormUsuarios(forms.ModelForm):

    class Meta:
        model = Usuarios
        fields = (
            "dni",
            "nombre",
            "apellido",
            "email",
            "direccion",
            "telefono",
            "contacto",
            )
        widgets = {
            "dni": forms.TextInput(attrs={"placeholder": "DNI", "class": "input-general"}),
            "nombre": forms.TextInput(attrs={"placeholder": "Nombre completo", "class": "input-general"}),
            "apellido": forms.TextInput(attrs={"placeholder": "Apellidos", "class": "input-general"}),
            "email": forms.TextInput(attrs={"placeholder": "Correo electrónico", "class": "input-general"}),
            "direccion": forms.TextInput(attrs={"placeholder": "Dirección", "class": "input-general"}),
            "telefono": forms.TextInput(attrs={"placeholder": "Teléfono", "class": "input-general"}),
            "contacto": forms.TextInput(attrs={"placeholder": "Número de contacto", "class": "input-general"})
            }