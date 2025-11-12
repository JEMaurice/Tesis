from django import forms
from .models import Cliente, Contacto_cliente

""" LO QUE SE MUESTRA EN LA WEB, DANDOLE CLASES ATRIBUTOS O PROPIEDADES A LAS ETIQUETAS QUE UTILIZAMOS """


class Formcontactocliente(forms.ModelForm):
    class Meta:
        model= Contacto_cliente
        fields= (
            "nombre",
            "telefono",
            )
        widgets  = {
            "nombre" : forms.TextInput(attrs={"placeholder" : "Ingresar aqui nombre", "class": "input-general"}),
            "telefono" : forms.TextInput(attrs={"placeholder" : "Ingresar aqui telefono contacto", "class": "input-general"}),
            }



class Formcliente(forms.ModelForm):
    class Meta:
        model= Cliente
        fields= (
            "cuit_o_cuil",
            "razon_social",
            "fantasia",
            "mail",
            "direccion",
            "telefono",
            "imagen",
            "contacto",
            "hoja_vida" 
            )
        widgets  = {
            "cuit_o_cuil" : forms.TextInput(attrs={"placeholder" : "Ingresar aqui CUIT/CUIL", "class": "input-general"}),
            "razon_social" : forms.TextInput(attrs={"placeholder" : "Ingresar aqui razon social", "class": "input-general"}),
            "fantasia" : forms.TextInput(attrs={"placeholder" : "Ingresar aqui nombre fantasia", "class": "input-general"}),
            "mail" : forms.TextInput(attrs={"placeholder" : "Ingresar aqui mail", "class": "input-general"}),
            "direccion" : forms.TextInput(attrs={"placeholder" : "Ingresar aqui direccion", "class": "input-general"}),
            "telefono" : forms.TextInput(attrs={"placeholder" : "Ingresar aqui telefono", "class": "input-general"}), 
            "imagen": forms.FileInput(attrs={'class':'form-control'}),
            "hoja_vida": forms.Textarea(attrs={'class':'input-general'}),
            "contacto": forms.Select(attrs={'class':'input-general seleccion'}),
            }
        
class Formupdatecliente(forms.ModelForm):
    class Meta:
        model= Cliente
        fields= (
            "cuit_o_cuil",
            "razon_social",
            "fantasia",
            "mail",
            "direccion",
            "telefono",
            "imagen",
            "contacto",
            "hoja_vida" 
            )
        widgets  = {
            "cuit_o_cuil" : forms.TextInput(attrs={"placeholder" : "Ingresar aqui CUIT/CUIL", "class": "input-general"}),
            "razon_social" : forms.TextInput(attrs={"placeholder" : "Ingresar aqui razon social", "class": "input-general"}),
            "fantasia" : forms.TextInput(attrs={"placeholder" : "Ingresar aqui nombre fantasia", "class": "input-general"}),
            "mail" : forms.TextInput(attrs={"placeholder" : "Ingresar aqui mail", "class": "input-general"}),
            "direccion" : forms.TextInput(attrs={"placeholder" : "Ingresar aqui direccion", "class": "input-general"}),
            "telefono" : forms.TextInput(attrs={"placeholder" : "Ingresar aqui telefono", "class": "input-general"}), 
            "hoja_vida": forms.Textarea(attrs={'class':'input-general'}),
            "contacto": forms.Select(attrs={'class':'input-general seleccion'}),
            }