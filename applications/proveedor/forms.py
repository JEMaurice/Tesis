from django import forms
from .models import Contacto_proveedores, Proveedores

""" LO QUE SE MUESTRA EN LA WEB, DANDOLE CLASES ATRIBUTOS O PROPIEDADES A LAS ETIQUETAS QUE UTILIZAMOS """


class Formcontactoproveedores(forms.ModelForm):
    class Meta:
        model= Contacto_proveedores
        fields= (
            "nombre",
            "telefono",
            )
        widgets  = {"nombre" : forms.TextInput(attrs={"placeholder" : "Ingresar aqui nombre", "class": "input-general"}),
                    "telefono" : forms.TextInput(attrs={"placeholder" : "Ingresar aqui telefono contacto", "class": "input-general"})
                    }



class Formproveedores(forms.ModelForm):
    class Meta:
        model= Proveedores
        #fields = "__all__"
        fields= (
            "cuit_o_cuil",
            "razon_social",
            "mail",
            "direccion",
            "telefono",
            "imagen",
            "contacto_proveedor",
            "hoja_vida",
            )
        widgets  = {"cuit_o_cuil" : forms.TextInput(attrs={"placeholder" : "Ingresar aqui CUIT/CUIL", "class": "input-general"}),
                    "razon_social" : forms.TextInput(attrs={"placeholder" : "Ingresar aqui razon social", "class": "input-general"}),
                    "mail" : forms.TextInput(attrs={"placeholder" : "Ingresar aqui mail", "class": "input-general"}),
                    "direccion" : forms.TextInput(attrs={"placeholder" : "Ingresar aqui direccion", "class": "input-general"}),
                    "telefono" : forms.TextInput(attrs={"placeholder" : "Ingresar aqui telefono", "class": "input-general"}), 
                    "imagen": forms.FileInput(attrs={'class':'form-control'}),
                    "contacto_proveedor": forms.Select(attrs={'class':'input-general seleccion'}),
                    "hoja_vida": forms.Textarea(attrs={'class':'input-general'}),                    
                    }
        
class Formupdateproveedores(forms.ModelForm):
    class Meta:
        model= Proveedores
        #fields = "__all__"
        fields= (
            "cuit_o_cuil",
            "razon_social",
            "mail",
            "direccion",
            "telefono",
            "imagen",
            "contacto_proveedor",
            "hoja_vida",
            )
        widgets  = {"cuit_o_cuil" : forms.TextInput(attrs={"placeholder" : "Ingresar aqui CUIT/CUIL", "class": "input-general"}),
                    "razon_social" : forms.TextInput(attrs={"placeholder" : "Ingresar aqui razon social", "class": "input-general"}),
                    "mail" : forms.TextInput(attrs={"placeholder" : "Ingresar aqui mail", "class": "input-general"}),
                    "direccion" : forms.TextInput(attrs={"placeholder" : "Ingresar aqui direccion", "class": "input-general"}),
                    "telefono" : forms.TextInput(attrs={"placeholder" : "Ingresar aqui telefono", "class": "input-general"}), 
                    "contacto_proveedor": forms.Select(attrs={'class':'input-general seleccion'}),
                    "hoja_vida": forms.Textarea(attrs={'class':'input-general'}),                    
                    }